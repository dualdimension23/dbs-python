import cx_Oracle
from typenv import Env
from typing import Union, Any, Dict, List
from util import utils
from modules.db import Database

env = Env()
env.read_env()
env.prefix.append("ORACLE_")


class OracleDatabase(Database):
    def __init__(self):
        cx_Oracle.init_oracle_client(lib_dir=env.str("INSTANT_CLIENT_PATH"))
        self.connection: Union[cx_Oracle.Connection, None] = None
        self.cursor: Any = None

    def connect(self, url: str) -> None:
        """
        Connects to database using an url.
        :param url: Url of the host, format: host:port/SID
        :return: None
        """
        self.connection = cx_Oracle.connect(user=env.str("USER"), password=env.str("PASSWORD"),
                                            dsn=url, encoding="UTF-8")
        self.cursor = self.connection.cursor()

    def execute(self, statement: str, values=None) -> bool:
        """
        Executes a SQL statement.
        :param values: Values to provide the statement, e.g. values for insertion
        :param statement: SQL statement in string format
        :return: True if no error occurred, else False
        """
        if values is None:
            values = dict()
        try:
            self.cursor.execute(statement, values)
        except cx_Oracle.DatabaseError as e:
            print(f"Error while execution of statement: {statement}", e)
        return self.connection.commit()

    def disconnect(self) -> None:
        """Closes the connection to the database."""
        self.connection.close()

    def select_all_from(self, table: str) -> List:
        """
        Executes a 'SELECT * FROM `table`' statement.
        :param table: Name of the table
        :return: None
        """
        try:
            self.execute(f"SELECT * FROM {table}")
        except Exception as e:
            print(f"Error while executing 'SELECT * FROM {table}' statement: ", e)

        result = self.cursor.fetchall()
        return result

    def insert_into(self, *, values: Union[List[Dict], Dict], table: str) -> None:
        """
        Executes a 'INSERT INTO `table`' statement.
        :param values: Values to be inserted
        :param table: Name of the table
        :return: None
        """
        if not isinstance(values, List):
            values = [values]
        for value in values:
            self.select_all_from(table)
            value_keys = utils.get_fields_repr(value, is_value=True)
            fields = utils.get_fields_repr(self.cursor.description)
            statement = f"INSERT INTO {table} {str(fields)} VALUES {str(value_keys)}"
            self.execute(statement, value)

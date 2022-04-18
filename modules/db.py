from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self, url: str) -> None:
        """Connects to database."""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """Closes the connection to the database."""
        pass

    @abstractmethod
    def execute(self, statement: str, values=None) -> bool:
        """Executes a SQL statement."""
        pass

    def __del__(self):
        """Close connection."""
        self.disconnect()
        print("Disconnected from db.")


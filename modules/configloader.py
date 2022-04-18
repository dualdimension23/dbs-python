import yaml


class ConfigLoader:
    def __init__(self, config_path: str = "config.yaml"):
        self.config_file = yaml.safe_load(open(config_path))

    @classmethod
    def get_data_path(cls, subpath: str):
        instance = cls()
        return instance.config_file["paths"][subpath]


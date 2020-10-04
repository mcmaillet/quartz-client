from config import *


class ConfigReader:
    def __init__(self):
        import configparser
        config = configparser.ConfigParser()
        config.read(ENVIRONMENT)

        self.default_config = config['DEFAULT']

    def get(self, key):
        return self.default_config.get(key, None)

    def get_boolean(self, key):
        return self.default_config.getboolean(key)

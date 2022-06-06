import configparser

_CONFIG_FILENAME = "config.ini"

_CONFIG = configparser.ConfigParser()
_CONFIG.read(_CONFIG_FILENAME)

HOSTNAME = _CONFIG["rcon_config"]["host"]
PORT = _CONFIG["rcon_config"]["port"]
PASSWORD = _CONFIG["rcon_config"]["password"]

import configparser
import os

config = configparser.ConfigParser()

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Correct path to config.ini
config_path = os.path.join(BASE_DIR, "config", "config.ini")

config.read(config_path)

def configuration(key, value):
    """
    Fetch a configuration value from config.ini file

    :param key: Section name in config.ini (e.g., 'URL')
    :param value: Key inside the section (e.g., 'base_url')
    :return: Configuration value as string
    """

    # Return the requested value from the configuration file
    return config.get(key, value)


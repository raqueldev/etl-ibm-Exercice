import configparser
from pathlib import Path


def get_config():
    c = configparser.ConfigParser()
    c.read('../webster/config/config.ini')
    return c

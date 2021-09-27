# config.py Parse all arrangement from the ini file

import os
from pathlib import Path
from configparser import ConfigParser

ARRANGE_FILE = next(Path.cwd().parent.glob('*.ini'))

parser = ConfigParser()
parser.read(ARRANGE_FILE)


def api_config(section):
    """Parse api config params. Return list ulrs"""

    params = parser.options(section)

    return [parser[section][param] for param in params]


def db_config(section):
    """Parse all config params required for db. Returns dict with config fields."""

    params = parser.options(section)
    params_dict = {}
    for param in params:
        # Password is saved as environment var
        if param == 'password':
            value = parser.get(section, param, vars=os.environ)
        else:
            value = parser.get(section, param)
        params_dict[param] = value

    return params_dict

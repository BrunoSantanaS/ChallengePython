import os

import requests

from utils import files

# Configuring Directories
# This first step of configuration will ensure that this code can run in any directory that you cloned the repository by utilizing relative paths
# Decided to utilize the OS library for creating paths in order to avoid errors if this code run in diferent Operational Systems (Linux, Windows and etc.)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(ROOT_DIR, 'challenge_2', 'config')

# Reading config file. The file must be updated with your personal keys for accessing the API
config_file = os.path.join(CONFIG_DIR, 'config.json')
config_parameters = files.read_config_json(config_file)
print(config_parameters)
# input('Please the city: ')
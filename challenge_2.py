import os

import requests

from utils import files

# Configuring Directories
# This first step of configuration will ensure that this code can run in any directory that you cloned the repository by utilizing relative paths
# Decided to utilize the OS library for creating paths in order to avoid errors if this code run in diferent Operational Systems (Linux, Windows and etc.)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(ROOT_DIR, 'challenge_2', 'config')

def print_data_to_console(info:dict) -> None:

    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    temp = data['main']['temp']

    print('Selected City:', data['name'])
    print('Temperature:', temp, '°C')
    print('Temperature Min:', data['main']['temp_min'], '°C')
    print('Temperature max:', data['main']['temp_max'], '°C')
    print('Humidity: ',humidity)
    print('Description:', description)

# Reading config file. The file must be updated with your personal keys for accessing the API
config_file = os.path.join(CONFIG_DIR, 'config.json')
config_parameters = files.read_config_json(config_file)

# This code will be keeping asking for new cities until the user is satisfied
while True:
    city = input('Please select the city: ')
    END_POINT = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config_parameters['api_key']}&units=metric"

    response = requests.get(END_POINT)
    data = response.json()

    # Print if the city is not found
    if data['cod'] == 404:
        print('City not found')
    elif data['cod'] == 200:
        print_data_to_console(data)
    else:
        print('Unexpected error')
        print('Closing Project')
        break

    searching = input('Press any key to continue or "q" to quit: ')
    if searching == 'q':
        print('Thank you for utilizing the API Wheather!')
        break
    else:
        print('-------Searching for another city------- \n\n')
        continue

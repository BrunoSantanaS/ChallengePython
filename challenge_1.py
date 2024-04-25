import os
import traceback

import pandas as pd

from utils import log, files

# Configuring Directories
# This first step of configuration will ensure that this code can run in any directory that you cloned the repository by utilizing relative paths
# Decided to utilize the OS library for creating paths in order to avoid errors if this code run in diferent Operational Systems (Linux, Windows and etc.)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_DIR = os.path.join(ROOT_DIR, 'challenge_1')
FILE_PATH = os.path.join(SAMPLE_DIR, 'transacoes.csv')

COLUMNS_EXPECTED = ['NOME DO CLIENTE', 'VALOR DA TRANSAÇÃO', 'DATA DA TRANSAÇÃO']
FILTERED_VALUE = 1000

# Load the data
try:
    print('Reading CSV File')
    data = pd.read_csv(FILE_PATH, sep=',')

# Error handling: File does not exist
except FileNotFoundError as error:
    log.create_log_file(SAMPLE_DIR, error)
    exit()

# Error handling: File in usage or not allowed to open
except PermissionError as error:
    log.create_log_file(SAMPLE_DIR, error)
    exit()

# Error handling: Unmapped error
except Exception as error:
    log.create_log_file(SAMPLE_DIR, error)
    exit()

# Normalizing columns
data.columns = data.columns.str.upper()

# Check if all columns are found in the file
if not files.check_columns(COLUMNS_EXPECTED, data):
    log.create_log_file(SAMPLE_DIR, 'Columns not found or differ from expected')
    exit()

# Filter values that are above the threshold for the expected column
filtered_data = data[data[COLUMNS_EXPECTED[1]] > FILTERED_VALUE]

# Save filtered data into a new CSV File
filtered_data.to_csv(r'sample_1\transacoes_altas.csv', index=False)
print('----------- End of Execution -----------')

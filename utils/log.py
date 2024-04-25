from datetime import datetime
import os

import traceback

def create_log_file(folder_path, error):
    error = traceback.format_exc()
    date_str = datetime.now().strftime('%y_%m_%d_%H_%M_%S')

    file_path = os.path.join(folder_path, f'log_{date_str}.txt')

    with open(file_path, 'w') as f:
        f.write('Log File -> TRACEBACK IMPLEMENTATION\n')
        f.write(f'Created on: {date_str}\n')
        f.write(f'Error: {error}\n')

    print('----------- End of Execution Due to Errors -----------')
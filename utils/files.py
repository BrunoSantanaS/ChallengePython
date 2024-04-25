import json

import pandas as pd

def check_columns(columns:list, dataframe:pd.DataFrame) -> bool:
    """
    It will check all the columns exist in the dataframe
    Normalizing the column found in the dataframe
    """
    for item in columns:
        if item not in dataframe.columns.str.upper():
            return False

    return True

def read_config_json(filepath:str) -> dict:
    """
    It will read the config JSON file in the directory
    """
    return json.load(open(filepath))
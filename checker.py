import logging
import pandas as pd
from data.getter import get_data

def get_path():
    try:
        path = get_data()
        return path
    except Exception as e:
        logging.error(e)
        return None

if __name__ == "__main__":
    x = get_path()
    if x:
        print(f"Data downloaded successfully @ {x}")
    else:
        print("Failed to download data")
    
    
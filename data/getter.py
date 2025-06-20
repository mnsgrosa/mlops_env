import kagglehub
import os
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

def get_data():
    load_dotenv()

    try:
        path = kagglehub.dataset_download("khushikyad001/china-water-pollution-monitoring-dataset")
        logging.info(f"Data downloaded successfully @ {path}")
        return path
    except Exception as e:
        logging.error(e)
        return None
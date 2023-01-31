import logging
from src.utils import save_json
import time
from src import logging
from src.constants import *
from src.components import DataIngestionPreparation


STAGE = "Stage 1, Data Ingestion and Preparation" ## <<< change stage name 

# init logger


def main():
    data_ing_prep_obj = DataIngestionPreparation()
    data_ing_prep_obj.load_data()


if __name__ == '__main__':
    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main()
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e
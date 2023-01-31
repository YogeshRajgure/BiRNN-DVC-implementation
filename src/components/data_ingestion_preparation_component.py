import tensorflow_datasets as tfds
from src.constants import *
import tensorflow as tf
from src import logging
import os

class DataIngestionPreparation:
    def __init__(self):
        self.dataset_name = "imdb_reviews"

    def load_data(self,):
        dataset, info = tfds.load(
                                name=self.dataset_name, 
                                with_info=True, 
                                as_supervised=True, 
                                data_dir = os.path.join("data"))
        
        self.train_ds, self.test_ds = dataset["train"], dataset["test"]
        logging.info(f"{self.dataset_name} dataset downloaded with info:\n{info}")

    
    def shuffle_and_batch(self):
        self.train_ds = self.train_ds.shuffle()
        train_ds = train_ds.shuffle(Confi)

    # def 
import tensorflow_datasets as tfds
from src.constants import *
import tensorflow as tf
from src import logging
import os
from src.utils import save_bin

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
        self.train_ds = self.train_ds.shuffle(TRAINING_BUFFER_SIZE).batch(TRAINING_BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
        self.test_ds = self.test_ds.shuffle(TRAINING_BUFFER_SIZE).batch(TRAINING_BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
        logging.info("datasets are now shuffeled and batched")

    def encode_on_training_data(self):
        self.encoder = tf.keras.layers.TextVectorization(max_tokens=VOCAB_SIZE)
        self.encoder.adapt(self.train_ds.map(lambda text, label:text))
        logging.info("encoding done")
    
    def _save_encoder(self):
        save_bin(data=self.encoder, path = os.path.join("artifacts", "encoder.bin"))
    
    def _save_train_test_ds(self):
        save_bin(data=self.train_ds, path = os.path.join("artifacts", "test_ds.bin"))
        save_bin(data=self.test_ds, path = os.path.join("artifacts", "test_ds.bin"))
    
    def save_artifacts(self):
        self._save_encoder()
        self._save_train_test_ds()
        logging.log(f"artifacts saved successfuly")
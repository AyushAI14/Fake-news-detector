import os
import pandas as pd
from src.logging import logger
from src.entity import DataIngestionConfig
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

class DataIngestion:
    def __init__(self,config=DataIngestionConfig):
        self.config=config
        

    def get_data(self):
        """
        Downloads dataset from Kaggle and saves it locally.
        """
        try:
            api.dataset_download_files(
                dataset=self.config.source_path,
                path=self.config.local_file_dir,
                unzip=True
            )
            logger.debug('Data successfully fetched from Kaggle')
        except Exception as e:
            logger.error(f"Failed to download data: {e}")
            raise e
    def concat_data(self):
        """
        Concatenates the fake and true CSV files into one DataFrame, shuffles it, and saves it.
        """
        try:
            # Load CSVs into DataFrames
            true_df = pd.read_csv(self.config.true_data)
            fake_df = pd.read_csv(self.config.fake_data)
            true_df['label']=1
            fake_df['label']=0

            # Concatenate and shuffle
            df = pd.concat([true_df, fake_df], ignore_index=True)
            df = df.sample(frac=1, random_state=42).reset_index(drop=True)

            # Save the final DataFrame
            df.to_csv(self.config.df_output_path, index=False)
            logger.debug('Data successfully concatenated and saved.')
        except Exception as e:
            logger.error(f"Failed to concatenate data: {e}")
            raise e

     
from src.constants import *
from src.utils.common import read_yaml_file,create_dir
from src.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,config=CONFIG_FILE_PATH,
                 param=PARAM_FILE_PATH):
        self.config=read_yaml_file(config)
        self.param=read_yaml_file(param)
        create_dir([self.config.root_Artifact])

    def getDataIngestion(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_dir([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_path=config.source_path,
            local_file_dir=Path(config.local_file_dir),
            true_data=Path(config.true_data),
            fake_data=Path(config.fake_data),
            df_output_path = Path(config.df_output_path)
        )
        return data_ingestion_config
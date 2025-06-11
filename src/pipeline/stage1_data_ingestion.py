from src.config.configuration import ConfigurationManager
from src.components.dataIngestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self):
        pass

    def intiate_data_ingestion(self):
        config=ConfigurationManager()
        getDataIngestionConfig = config.getDataIngestion()
        dataingestion = DataIngestion(config=getDataIngestionConfig)
        dataingestion.get_data()
        dataingestion.concat_data()
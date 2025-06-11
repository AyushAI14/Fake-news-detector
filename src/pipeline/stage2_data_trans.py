from src.components.datatransformation import DataTransformation
from src.config.configuration import ConfigurationManager

class DataTransformationPipeline:
    def __init__(self):
        pass

    def intiate_data_transformation(self):
        config=ConfigurationManager()
        getDataTransConfig = config.getDataTransformation()
        dataTranfrom = DataTransformation(config=getDataTransConfig)
        dataTranfrom.tranform_text()
from src.pipeline.stage1_data_ingestion import DataIngestionPipeline
from src.pipeline.stage2_data_trans import DataTransformationPipeline
from src.logging import logger

STAGE_NAME = 'Data ingestion stage'

try:
    logger.info(f'Initiating {STAGE_NAME} intiated')
    Data_Ingestion_Pipeline = DataIngestionPipeline()
    Data_Ingestion_Pipeline.intiate_data_ingestion()
    logger.info(f'{STAGE_NAME} initiated')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Transformation stage'

try:
    logger.info(f'Initiating {STAGE_NAME} intiated')
    Data_Transformation_Pipeline = DataTransformationPipeline()
    Data_Transformation_Pipeline.intiate_data_transformation()
    logger.info(f'{STAGE_NAME} initiated')
except Exception as e:
    logger.exception(e)
    raise e


    
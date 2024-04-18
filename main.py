from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
STAGE_NAME ="Data Ingestion Stage"

try:
    logger.info(f">>>>Starting {STAGE_NAME} <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> Completed {STAGE_NAME} <<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME ="Data Validation Stage"

try:
    logger.info(f">>>>Starting {STAGE_NAME} <<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>> Completed {STAGE_NAME} <<<<")
except Exception as e:
    logger.exception(e)
    raise e
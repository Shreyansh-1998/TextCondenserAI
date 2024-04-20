from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from src.textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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

STAGE_NAME ="Data Transformation Stage"

try:
    logger.info(f">>>>Starting {STAGE_NAME} <<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>> Completed {STAGE_NAME} <<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME ="Model Training Stage"

try:
    logger.info(f">>>>Starting {STAGE_NAME} <<<<")
    model_training = ModelTrainerPipeline()
    model_training.main()
    logger.info(f">>>> Completed {STAGE_NAME} <<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
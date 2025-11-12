from MyProject.Pipeline.stage01 import DataIngestionTrainingPipeline
from MyProject.Pipeline.stage02 import DataValidationTrainingPipeline
from MyProject.Pipeline.stage03 import DataTransformationTrainingPipeline
from MyProject.Pipeline.stage04 import ModelTrainerTrainingPipeline
from MyProject.Pipeline.stage05 import ModelEvaluationTrainingPipeline
from MyProject.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    
    logger.exception(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e



STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Trainer stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
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
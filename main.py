from MyProject.Pipeline.stage01 import dataIngestionPipeline 
from MyProject.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = dataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e
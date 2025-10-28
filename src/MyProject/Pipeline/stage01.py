from MyProject.config.configuration import ConfigManager
from MyProject.components.data_ingestion import data_ingestion
from MyProject.logging import Logger



class dataIngestionPipeline:
    def __init__(self):
        self.config = ConfigManager.get_data_ingestion_config()
        self.logger = Logger.get_logger()

    def start_data_ingestion(self):
        self.logger.info("Starting data ingestion process.")
        ingestion_component = data_ingestion.DataIngestionComponent(self.config)
        ingestion_component.execute()
        self.logger.info("Data ingestion process completed.")


    def main(self):
        config_manager = ConfigManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        downloaded_file=data_ingestion.download_data()
        data_ingestion.extract_zip_file(downloaded_file)
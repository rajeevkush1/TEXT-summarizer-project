import os
import urllib.request as request
import zipfile
from MyProject.logging import logger
from MyProject.utils.common import get_size
from pathlib import Path
from MyProject.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self) -> Path:
        logger.info("Starting data download...")
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                self.config.source_URL, 
                self.config.local_data_file
            )
            logger.info(f"Data downloaded successfully and saved to {filename} with size {get_size(Path(filename))}")
        else:
            logger.info("Data file already exists. Skipping download.")
        return self.config.local_data_file
    
    def extract_zip_file(self, zip_file_path: Path | None = None):
        logger.info("Starting data extraction...")
        zip_path = Path(zip_file_path) if zip_file_path is not None else Path(self.config.local_data_file)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info(f"Data extracted successfully to {self.config.unzip_dir}")
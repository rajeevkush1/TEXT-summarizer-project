from MyProject.config.configuration import ConfigManager
from MyProject.components.data_validation import DataValidation
from MyProject.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        data_validation_config = config.get_data_validation_config()
        validator = DataValidation(config=data_validation_config)
        validator.validate_all_files_exist()


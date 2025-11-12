from MyProject.config.configuration import ConfigManager
from MyProject.components.data_transformation import DataTransformation
from MyProject.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
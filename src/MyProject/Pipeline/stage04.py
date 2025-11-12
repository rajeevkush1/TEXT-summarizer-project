from MyProject.config.configuration import ConfigManager
from MyProject.components.model_trainer import ModelTrainer
from MyProject.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
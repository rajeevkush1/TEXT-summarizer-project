from MyProject.config.configuration import ConfigManager
from MyProject.components.model_evaluation import ModelEvaluation
from MyProject.logging import logger




class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        model_evaluation_config = config.get_model_evaluation_config()
        evaluator = ModelEvaluation(config=model_evaluation_config)
        evaluator.evaluate()
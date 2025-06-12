from src.components.model_evalution import ModelEvalution
from src.config.configuration import ConfigurationManager

class ModelEvalutionPipeline:
    def __init__(self):
        pass

    def intiate_model_eval(self,text):
        config=ConfigurationManager()
        getmodelevalConfig = config.getModelEvalution()
        modelEval = ModelEvalution(config=getmodelevalConfig)
        modelEval.predict(text)
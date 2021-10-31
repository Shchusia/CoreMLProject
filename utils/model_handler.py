from typing import Dict

from ml_lib import LGBM, MLModel, RandomForest

from .model_storage_handler import ModelStorageHandler


class ModelHandler:
    def __init__(self):
        self.storage = ModelStorageHandler()
        pass

    def extract_models(self, *args, **kwargs) -> Dict:
        pass

    def load_model(self, *args, **kwargs):
        pass


def init_models() -> Dict[str, MLModel]:
    mh = ModelHandler()
    # extract model
    mh.extract_models()
    # init models
    dict_models = {"lgbm": LGBM(), "random": RandomForest()}
    return dict_models

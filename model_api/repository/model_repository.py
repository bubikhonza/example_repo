import pickle
from functools import lru_cache
from typing import Any
import os

from sklearn.tree import DecisionTreeClassifier

from model_api.enums import ModelType


class ModelRepository:
    def __init__(self):
        self.__model_filepath = "/Users/bubikhonza/example_repo/model_api/models"

    @lru_cache
    def load_model(self, model_type: ModelType) -> DecisionTreeClassifier:
        with open(os.path.join(self.__model_filepath, f"{model_type.value}.pkl"), "rb") as file:
            loaded_model = pickle.load(file)

        return loaded_model
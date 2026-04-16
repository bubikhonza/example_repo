import pandas as pd
from fastapi.encoders import jsonable_encoder

from model_api.entities.ModelInfoResponse import ModelInfoResponse
from model_api.entities.predict_request import PredictRequest
from model_api.entities.predict_response import PredictResponse
from model_api.enums import ModelType
from model_api.repository.model_repository import ModelRepository


class ModelService:
    def __init__(self, model_repository: ModelRepository):
        self.__model_repository = model_repository

    def get_model_info(self, model_type: ModelType) -> ModelInfoResponse:
        model = self.__model_repository.load_model(model_type)
        return ModelInfoResponse(
            max_depth=model.max_depth,
            max_features=model.max_features if model.max_features else 0
        )

    def predict(self, model_type: ModelType, predict_request: PredictRequest) -> PredictResponse:
        model = self.__model_repository.load_model(model_type)
        input_df = pd.DataFrame([jsonable_encoder(predict_request)])
        result = list(model.predict(input_df))
        return PredictResponse(passenger_id=predict_request.PassengerId, survived=bool(result[0]))

from fastapi import APIRouter

from model_api.entities.model_info_response import ModelInfoResponse
from model_api.entities.predict_request import PredictRequest
from model_api.entities.predict_response import PredictResponse
from model_api.enums import ModelType
from model_api.repository.model_repository import ModelRepository
from model_api.service.model_service import ModelService

model_router = APIRouter()

model_service = ModelService(
    model_repository=ModelRepository()
)


@model_router.post("/predict/{model_type}")
def predict(model_type: ModelType, predict_request: PredictRequest) -> PredictResponse:
    """predikce se zvoleným modelem"""
    return model_service.predict(model_type, predict_request)


@model_router.get("/models/{model_type}")
def get_model(model_type: ModelType) -> ModelInfoResponse:
    """vypíše info o konkrétním vytrénovaném modelu"""
    return model_service.get_model_info(model_type)


def get_all_models() -> list:
    """vypíše seznam všech dostupných modelů k predikci"""
    # TODO: implement
    pass
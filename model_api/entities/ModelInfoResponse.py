from pydantic import BaseModel


class ModelInfoResponse(BaseModel):
    max_depth: int
    max_features: int
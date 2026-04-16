from pydantic import BaseModel


class PredictResponse(BaseModel):
    passenger_id: int
    survived: bool
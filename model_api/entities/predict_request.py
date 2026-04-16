from pydantic import BaseModel


class PredictRequest(BaseModel):
    PassengerId: int
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: float
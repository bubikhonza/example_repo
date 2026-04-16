import uvicorn
from fastapi import FastAPI

from model_api.controller.model_controller import model_router

app = FastAPI()
app.include_router(model_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
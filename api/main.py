from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

class RegisterRequest(BaseModel):
    username: str
    password: str
    email: str | None = None

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []

@app.get("/protected/{api_token}")
def protected(api_token: str):
    if api_token == "1234":
        return {"message": "Success"}
    else:
        return {"message": "Unauthorized"}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users")
def get_users():
    return {"users": users}

@app.post("/register")
def register(register_request: RegisterRequest):
    new_user = {
        "username": register_request.username,
        "password": register_request.password,
        "email": register_request.email
    }
    users.append(new_user)
    print(f"user {new_user} registered")
    return {"success": True}

@app.delete("/users/{user_name}")
def delete_user(user_name: str):
    for user in users:
        if user["username"] == user_name:
            users.remove(user)
            return {"success": True}
    return {"success": False, "message": "User not found"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/landing", response_class=HTMLResponse)
def get_landing(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"users": users}
    )
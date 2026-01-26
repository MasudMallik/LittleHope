from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define request body model
class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/")
def check(request: LoginRequest):
    if request.email == "abc@gmail.com" and request.password == "123":
        return {"login": "successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

from fastapi import FastAPI,Depends,Request
from backend.modules.user_valid import User_for_login,User_for_reg
from backend.modules.password_hash import hash_password,check_password
from backend.modules.token_create import create_token,decode_token
from fastapi.security import OAuth2PasswordBearer

outh2=OAuth2PasswordBearer(tokenUrl="token")

app=FastAPI(title="LittleHope",
            description="This platform is a community-driven initiative designed to help reunite missing children with their families. Users can securely register and upload details of lost or missing children, including descriptions and relevant information, making them visible to the public.Visitors who recognize or find a missing child can quickly reach out to the concerned family through the provided contact details. By combining technology with collective awareness, this platform aims to create hope, speed up searches, and bring children back to where they belong — home",
            summary="Every child deserves to be safe and at home.",
            version="0.0.0.1",
            )
@app.post("/token")
async def user_token(request:Request):
    data=await request.json()
    token=create_token(data)
    return {"token":token,"access_type":"bearer"}

@app.post("/login")
async def login(request:Request,token:str=Depends(outh2)):
    try:
        data=decode_token(token)
    except Exception as e:
        return e
    else:
        return {"data":data}

@app.post("/register")
async def new_user(user:User_for_reg):
    return {"user_details":"successfully created"}
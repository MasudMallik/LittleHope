from fastapi import FastAPI,Depends,Request
from backend.modules.user_valid import User_for_login,User_for_reg
from backend.modules.password_hash import hash_password,check_password
from backend.modules.token_create import create_token,decode_token
from fastapi.security import OAuth2PasswordBearer
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

client=MongoClient(os.getenv("mongo_db_string"))


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
    new_hash_pw=hash_password(user.password)
    db=client["user_db"]
    collection=db["all_users"]
    exist=collection.find_one({"email":user.email})
    if exist:
        return {"user_details":"you already have an account please login"}
    collection.insert_one({"name":user.name,"email":user.email,"contact":user.contact_no,"state":user.state,"district":user.district,"password":new_hash_pw})
    return {"user_details":"successfully created","details":{"name":user.name}}
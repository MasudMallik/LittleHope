from fastapi import FastAPI,Depends,Request,HTTPException
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
async def login(user:User_for_login):
    db=client["user_db"]
    collections=db["all_users"]
    k=collections.find_one({"email":user.email})
    if not k:
        return {"login":False}
    else:
        if(check_password(user.password,k.get("password"))):
            return {"login":True,"name":k.get("name"),"email":k.get("email"),"state":k.get("state"),"district":k.get("district")}
        else:
            return {"login":True,"error":"password didnt match"}

@app.post("/register")
async def new_user(user:User_for_reg):
    new_hash_pw=hash_password(user.password)
    db=client["user_db"]
    collection=db["all_users"]
    exist=collection.find_one({"email":user.email})
    if exist:
        return {"user_details":"True"}
    collection.insert_one({"name":user.name,"email":user.email,"contact":user.contact_no,"state":user.state,"district":user.district,"password":new_hash_pw})
    return {"user_details":"successfully created"}

@app.post("/get_user_details")
async def get_user_det(request:Request,token:str=Depends(outh2)):
    try:
        data=decode_token(token=token)
    except Exception:
        return {"token":"not decoded"}
    else:
        return {"data":data}
@app.put("/update_user_det")
async def update_user_info(request:Request,token:str=Depends(outh2)):
    new_data=await request.json()
    db=client["user_db"]
    collection=db["all_users"]
    try:
        collection.update_one({"email":new_data["email"]},
                              {"$set": {"name":new_data["name"],"district":new_data["district"],"state":new_data["state"]} })
    except Exception:
        return{"update":False}
    else:
        return{"update":True}
    

@app.put("/update_password")
async def update_password(request:Request,token:str=Depends(outh2)):
    data=await request.json()
    db=client["user_db"]
    collection=db["all_users"]
    k=collection.find_one({"email":data["email"]})
    print(data["old_password"])
    if check_password(data["old_password"],k["password"]):
        temp=hash_password(data["new_password"])
        result=collection.update_one({"email":data["email"]},{
                "$set": {"password":temp}
        })
        return {"password_update":True}
    else:
        return {"password_update":False}
        

@app.post("/new_case")
async def new_case(request:Request,token:str=Depends(outh2)):
    data=await request.json()
    print(data["child_info"])
    return {"data":data}
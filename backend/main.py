from fastapi import FastAPI,Depends,Request,HTTPException
from backend.modules.user_valid import User_for_login,User_for_reg
from backend.modules.password_hash import hash_password,check_password
from backend.modules.token_create import create_token,decode_token
from fastapi.security import OAuth2PasswordBearer
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
import os
from supabase import create_client,client
load_dotenv()

cli=MongoClient(os.getenv("mongo_db_string"))
supabase: client=create_client(os.getenv("supabase_url"),os.getenv("supabase_anomkey"))

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
    db=cli["user_db"]
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
    db=cli["user_db"]
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
    db=cli["user_db"]
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
    db=cli["user_db"]
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
    try:
        data=await request.json()
        user=decode_token(token)
        db=cli["reported_cases"]
        collection=db[user["name"]]
        collection.insert_one(data)
    except Exception:
        return {"status_of_upload":False}
    else:
        return {"status_of_upload":True}
    
@app.delete("/delete_user")
async def del_user(token:str=Depends(outh2)):
    try:
        user=decode_token(token)
        db=cli["user_db"]
        collections=db["all_users"]
        collections.delete_one({"email": user["email"]})
        db=cli["reported_cases"]
        print(user["name"])
        db.drop_collection(user["name"])
    except Exception:
        return {"delete":False}
    else:
        return {"delete":True}
    
@app.get("/your_posts")
async def all_posts(token:str=Depends(outh2)):
    user=decode_token(token)
    db=cli["reported_cases"]
    collections=db[user["name"]]

    if user["name"] not in db.list_collection_names():
        return {"posts": False}
    else:
        data=list(collections.find())
        for d in data:
            d["_id"]=str(d["_id"])
        return {"posts":True,"all_posts":data}

@app.delete("/delete_post/{id}")
async def delete_post(id:str,token:str=Depends(outh2)):
    user=decode_token(token)
    db=cli["reported_cases"]
    collections=db[user["name"]]
    file_path=collections.find_one({"_id":ObjectId(id)})
    res=supabase.storage.from_(os.getenv("bucket")).remove(file_path["other"].get("file_path"))
    try:
        collections.delete_one({"_id":ObjectId(id)})
    except Exception:
        return {"delete_post":False}
    else:
        return{"delete_post":True}

@app.get("/all_posts")
def all_posts():
    db=cli["reported_cases"]
    collections=db.list_collection_names()
    result={}
    for coll in collections:
        collection=db[coll]
        docs=list(collection.find())
        for doc in docs:
            doc["_id"] = str(doc["_id"])
        result[coll]=docs
    return {"result":result}
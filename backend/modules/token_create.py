from jwt import encode,decode
import datetime
from dotenv import load_dotenv
import os
load_dotenv()

def create_token(data:dict)->str:
    copy_of_data=data.copy()
    iat_time=datetime.datetime.utcnow()
    exp=datetime.datetime.utcnow()+datetime.timedelta(minutes=20)
    copy_of_data["iat"]=iat_time
    copy_of_data["exp"]=exp
    token=encode(copy_of_data,os.getenv("secret_key"),algorithm=os.getenv("algorithm"))
    return token

def decode_token(token:str)->dict | None:
    try:
        data=decode(token,os.getenv("secret_key"),algorithms=[os.getenv("algorithm")])
    except Exception:
        return None
    else:
        return data

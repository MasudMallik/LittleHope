from bcrypt import hashpw,checkpw,gensalt

def hash_password(password:str)->bytes:
    return hashpw(password.encode("UTF-8"),gensalt(12))

def check_password(password:str,hashed_pass:bytes)->bool:
    return checkpw(password.encode("UTF-8"),hashed_password=hashed_pass)
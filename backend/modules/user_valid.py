from pydantic import BaseModel,validator,EmailStr,Field
class User_for_reg(BaseModel):
    name:str=Field(...,description="name of the new user")
    email:EmailStr
    contact_no:str=Field(...)
    state:str=Field(...)
    district:str=Field()
    password:str=Field(...,min_length=4,max_length=20,description="password should contain atleast 1 uppercase,1 lowercase, 1 special character, 1 digit")
    
    @validator("password")
    def check_password(cls,password):
        hash={"uppercase":0,"lowercase":0,"special character":0,"digit":0}
        for i in password:
            if i.isdigit():
                hash["digit"]=1
            elif i.isalpha():
                if i.islower():
                    hash["lowercase"]=1
                else:
                    hash["uppercase"]=1
            else:
                hash["special character"]=1
        reasons=hash.values()
        if 0 in reasons:
            raise ValueError("password should contain atleast 1 uppercase,1 lowercase, 1 special character, 1 digit")
        else:
            return password
        
    @validator("contact_no")
    def check_contact(cls,contact):
        if len(contact)!=10:
            raise ValueError("give contact number withoud country code")
        return contact


class User_for_login(BaseModel):
    email:EmailStr
    password:str=Field(...,min_length=4,max_length=20,description="password should contain atleast 1 uppercase,1 lowercase, 1 special character, 1 digit")
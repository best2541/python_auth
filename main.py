from typing import Union
from fastapi import FastAPI,Header
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import jwt

app = FastAPI()

SECRET_KEY = "SDLFISEJFSNnsvisn2oi32no2nf"
ACCESS_TOKEN_EXPIRE_MINUTE = 800
dummy_user = {
    "username":"username",
    "password":"password"
}

class LoginClass(BaseModel):
    username:str
    password:str

@app.get("/")
def read_root():
    return  {"HI":"HI"}

@app.get("/id/{id}")
def read_id(id:int,q:Union[str,None] = None):
    return {"id":id,"q":q}

@app.post("/login")
async def login(login_item:LoginClass):
    data=jsonable_encoder(login_item)
    if dummy_user['username'] == data['username'] and dummy_user['password'] == data['password']:
        encode_jwt = jwt.encode(data,SECRET_KEY,algorithm="HS256")
        return {"token":encode_jwt}
    else:
        return {"token":"failed"}
@app.post("/auth")
async def auth(Authorization: str | None = Header(default=None)):
    decode_jwt = jwt.decode(Authorization, SECRET_KEY, algorithms=["HS256"])
    return {"decode":decode_jwt,"token":Authorization}

from fastapi import FastAPI, Depends, HTTPException

import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated


app = FastAPI()


oauth2_schema = OAuth2PasswordBearer(tokenUrl="token") #Guarda el token

#Diccionario de prueba
users = {
    "pablo":{"username":"pablo", "email":"pablo@gmail.com", "password":"1234"}, 
    "ana":{"username":"ana", "email":"ana@gmail.com", "password":"0987"}
}

#funcion para codificar el token
def encode_token(payload: dict) -> str:
    #el payload son los datos que se envian para guardar dentro del token (ej. username, email, password)
    #key: clave secreta para generar el token (normalmente se tiene un tiempo de expiracion)
    #algorithm: indica el tipo de algoritmo con el que se debe cifrar el token
    token = jwt.encode(payload=payload, key="secret-key", algorithm="HS256") 
    return token

#funcion para decodificar el token
def decode_token(token: Annotated[str, Depends(oauth2_schema)]) -> dict: 
    #Se obtiene el token a traves de la dependencia de oauth2_schema
    #Se pasa la misma clave secreta y una lista de los algoritmos para decodificar
    data = jwt.decode(token, "secret-key", algorithms=["HS256"])
    user = users.get(data["username"]) #Obtiene el usuario que coincida con el almacenado en el dict de prueba
    return user

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]): 
    #Obtiene el usuario que coincida con el almacenado en el dict de prueba
    user = users.get(form_data.username)
    #Obtiene el password que coincida con el almacenado en el dict de prueba
    passw = users.get(form_data.password)
    if not user and not passw:
        #Si alguno de los 2 no existe lanza el error
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    #token: primero envia un diccionario con los datos a guardar en el token que se generara
    #token: luego guarda el token generado por la funcion encode_token
    token = encode_token({"username": user["username"], "email":user["email"]})
    #retornamos el token en la vista
    return {"access_token":token}


@app.get("/user/profile")
def profile(my_user: Annotated[dict, Depends(decode_token)]): 
    return my_user
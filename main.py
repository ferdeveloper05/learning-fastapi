import json

from fastapi import FastAPI

app = FastAPI(title="Este es el Titulo")

def load_data(): 
    with open('patients.json', 'r') as file: 
        data = json.load(file)
    return data
    
@app.get("/")
def project(): 
    return {"message":"Sistema de gestion de pacientes"}

@app.get("/about")
def about(): 
    return {"message":"Un sistema de gestion de pacientes totalmente funcional"}

@app.get("/view")
def view():  
    data = load_data()
    return data
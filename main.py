from fastapi import FastAPI

app = FastAPI(title="Este es el Titulo")

@app.get("/")
def hello(): 
    return {"message":"Hello World"}


@app.get("/about")
def about(): 
    return {"message":"About FastAPI"}
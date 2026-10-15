from pydantic import BaseModel
from typing import Annotated, Optional


class Patient(BaseModel): 
    nombre: str
    edad: int
    genero: str
    peso: float
    altura: float
    alergias: list[str] | None

patient_info = {
    "nombre": "Carlos",
    "edad":"30", 
    "genero":"M", 
    "peso":60.5, 
    "altura":1.80, 
    "alergias":["Lactosa", "Polvo"]
}    
    
patient1 = Patient(**patient_info)

def present_patient(patient: Patient): 
    if isinstance(patient, Patient): 
        print(patient.nombre)
        print(patient.alergias)
        print(patient.edad)
        
present_patient(patient1)
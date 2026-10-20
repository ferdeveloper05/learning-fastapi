from typing import Annotated

from pydantic import BaseModel, Field


class Patient(BaseModel): 
    nombre: Annotated[str, Field(..., max_digits=50, title="Nombre del paciente", description="Describa el nombre del paciente en minimo 50 caracteres")]
    edad: int = Field(gt=0, lt=120)
    genero: str
    peso: Annotated[float, Field(gt=0, strict=True)]
    altura: Annotated[float, Field(gt=0, lt=3.0)]
    alergias: Annotated[list[str] | None, Field(default=None, description="Indique las alergias del paciente")]

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
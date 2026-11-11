from pydantic import BaseModel, EmailStr, Field, HttpUrl

from typing import Annotated


class Patient(BaseModel): 
    name: Annotated[str, Field(max_length=50, title="Nombre del paciente", description="Ingrese el nombre del paciente en menos de 50 caracteres", examples=["Shubham", "Arun"])]
    email: EmailStr
    linkedin_url: HttpUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description="El paciente es casado?")]
    allergys: Annotated[list[str]| None, Field(default=None, max_length=10)]
    contact_details: dict[str, str]
    
def update_patient_data(patient: Patient): 
    if isinstance(patient, Patient): 
        print(patient.name)
        print(patient.age)
        print(patient.allergys)
        print(patient.married)
        print("Actualizado en la base de datos")
        
patient_info = {
    "name":"shubham", 
    "email":"abc@gmail.com", 
    "linkedin_url":"https://linkedin.com/in/shubham", 
    "age":"20", 
    "weight":60, 
    "married":False, 
    "allergies":['dust', 'oil'], 
    "contact_details":{'phone':'0412000000'}
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)
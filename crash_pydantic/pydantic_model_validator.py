from pydantic import BaseModel, EmailStr, model_validator


class Patient(BaseModel): 
    name: str
    email: EmailStr
    age: str
    weight: float
    married: bool
    allergys: list[str]
    contact_details: dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):  
        if model.age > 60 and 'emergency' not in model.contact_details: 
            raise ValueError("Los pacientes mayores de 60 años deben tener un contacto de emergencia")
        return model
    
    
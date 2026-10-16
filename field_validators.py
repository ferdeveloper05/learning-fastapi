from pydantic import BaseModel, EmailStr, field_validator


class Patient(BaseModel): 
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact_details: dict[str, str]
    
    @field_validator('name')
    @classmethod
    def transform_name(clas, value: str): 
        return value.upper()
    
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
print(patient1.name)
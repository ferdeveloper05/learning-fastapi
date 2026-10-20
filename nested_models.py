# Los modelos anidados nos permiten organizar estructuras de datos complejas colocando un modelo Pydantic dentro de otro.

from pydantic import BaseModel


class Address(BaseModel): 
    city: str
    state: str
    pin: str
    

class Patient(BaseModel): 
    name: str
    gen: str
    age: int
    address: Address
    
addres_dict = {
    'city': 'Dist. Capital', 
    'state': 'Caracas', 
    'pin': '1030'
}

address1 = Address(**addres_dict)

patient_info = {
    'name':'Fer', 
    'gen':'Femenino', 
    'age':'25', 
    'address':address1
}

patient1 = Patient(**patient_info)

temp = patient1.model_dump(include="")

print(type(temp))
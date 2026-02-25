from pydantic import BaseModel

class PatientCreate(BaseModel):
    name: str
    age: int
    diagnosis: str

class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    diagnosis: str
    risk_level: str

    class Config:
        from_attributes = True

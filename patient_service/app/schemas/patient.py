import re
from pydantic import validator, field_validator
from app.schemas.base import CustomBaseModel
from uuid import UUID

class Patient(CustomBaseModel):
    first_name: str
    last_name: str
    age: int
    condition: str

    @validator('first_name', 'last_name')
    def validate_first_and_last_name(cls, value):
        # if not re.match("\b([A-ZÀ-ÿ][-,a-z. ']+[ ]*)+", value):
        if not re.match(".*", value):
            raise ValueError('Invalid first_name parameter')
        return value
  
    
    @field_validator('age')
    def validate_age_range(cls, value):
        if value not in range(0, 150):
            raise ValueError('Invalid age parameter')
        return value
  
class PatientOutput(Patient):
    # id: int
    id: UUID
    
    class Config:
        orm_mode=True
    
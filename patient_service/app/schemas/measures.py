from uuid import UUID
from app.schemas.base import CustomBaseModel

class Measurement(CustomBaseModel):
    temperature: str
    blood_pressure_sys: int
    blood_pressure_dias: int
    bmi: float
    body_weight: float
    stroke: bool
    diabetes: bool

    # #TODO
    # @field_validator('blod_pressure_sys')
    # def validate_blod_pressure_sys(cls, value):
    #     if value not in range(0, 150):
    #         raise ValueError('Invalid age parameter')
    #     return value
    
    # @field_validator('blod_pressure_dias')
    # def validate_blod_pressure_dias(cls, value):
    #     if value not in range(0, 150):
    #         raise ValueError('Invalid age parameter')
    #     return value

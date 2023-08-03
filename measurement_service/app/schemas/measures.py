from uuid import UUID
from app.schemas.base import CustomBaseModel
from pydantic import validator, field_validator

class Measurement(CustomBaseModel):
    temperature_celsius: float
    blood_pressure_sys: int
    blood_pressure_dias: int
    body_weight: float
    height_cm: float
    stroke: bool
    diabetes: bool
    patient_id: UUID

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


class MeasurementOutput(Measurement):
    # id: int
    id: UUID
    
    class Config:
        orm_mode=True
    
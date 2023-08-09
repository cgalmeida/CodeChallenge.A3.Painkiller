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

class MeasurementOutput(Measurement):
    # id: int
    id: UUID
    
    class Config:
        orm_mode=True
    
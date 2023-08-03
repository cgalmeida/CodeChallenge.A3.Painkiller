from sqlalchemy import Column, Integer, String, UUID, Float, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid

class Measurements(Base):
    __tablename__ = 'measurements'
    id = Column('measurement_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    temperature_celsius = Column('temperature_celsius', Float, nullable=False)
    blood_pressure_sys = Column('blood_pressure_sys', Integer, nullable=True)
    blood_pressure_dias = Column('blood_pressure_dias', Integer, nullable=True)
    body_weight = Column('body_weight', Float, nullable=False)
    height_cm = Column('height_cm', Integer, nullable=False)
    stroke = Column('stroke', Boolean, nullable=True, default=False)
    diabetes = Column('diabetes', Boolean, nullable=True, default=False)
    created_at = Column('created_at', DateTime, server_default=func.now())
    patient_id = Column('patient_id', UUID(as_uuid=True), nullable=False)
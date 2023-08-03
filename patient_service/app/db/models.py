from sqlalchemy import Column, Integer, String, UUID, Float, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid

class Patient(Base):
    __tablename__ = 'patients'
    id = Column('patient_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column('first_name', String, nullable=False)
    last_name = Column('last_name', String, nullable=False)
    age = Column('age', Integer, nullable=False)
    condition = Column('condition', String, nullable=True)
    measurements = relationship('Measurement', back_populates='patients')

class Measurement(Base):
    __tablename__ = 'measurements'
    id = Column('measurement_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    temperature = Column('temperature', String, nullable=False)
    blood_pressure_sys = Column('blood_pressure_sys', Integer, nullable=True)
    blood_pressure_dias = Column('blood_pressure_dias', Integer, nullable=True)
    bmi = Column('BMI', Float, nullable=True)
    body_weight = Column('body_weight', Float, nullable=False)
    stroke = Column('stroke', Boolean, nullable=True, default=False)
    diabetes = Column('diabetes', Boolean, nullable=True, default=False)
    created_at = Column('created_at', DateTime, server_default=func.now())
    patient_id = Column('patient_id', ForeignKey('patients.patient_id'), nullable=False)
    patients = relationship('Patient', back_populates='measurements')
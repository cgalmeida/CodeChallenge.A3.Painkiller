from sqlalchemy import Column, Integer, String, UUID, Float, DateTime, Boolean, func
from app.db.base import Base
import uuid

class Patient(Base):
    __tablename__ = 'patients'
    id = Column('patient_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column('first_name', String, nullable=False)
    last_name = Column('last_name', String, nullable=False)
    age = Column('age', Integer, nullable=False)
    condition = Column('condition', String, nullable=True)
    # measurements = relationship('Measurement', back_populates='patients')

    def to_dict(self):
        return {
            'id ': self.id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'age' : self.age,
            'condition' : self.condition
        }

class Measurement(Base):
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
    # patients = relationship('Patient', back_populates='measurements')

    def to_dict(self):
        return {
            'id ': self.id,
            'temperature_celsius': self.temperature_celsius,
            'blood_pressure_sys': self.blood_pressure_sys,
            'blood_pressure_dias': self.blood_pressure_dias,
            'body_weight': self.body_weight,
            'height_cm': self.height_cm,
            'stroke': self.stroke,
            'diabetes': self.diabetes,
            'created_at': self.created_at,
            'patient_id': self.patient_id
        }

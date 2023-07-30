from sqlalchemy import Column, Integer, String, UUID
from app.db.base import Base
import uuid

class Patient(Base):
    __tablename__ = 'patients'
    id = Column('patient_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column('first_name', String, nullable=False)
    last_name = Column('last_name', String, nullable=False)
    age = Column('age', Integer, nullable=False)
    condition = Column('condition', String, nullable=True)
from sqlalchemy.orm import Session
from app.db.models import Patient as PatientModel
from app.schemas.patient import Patient, PatientOutput
from app.usecases.measurement import MeasurementUseCases
from fastapi.exceptions import HTTPException
from fastapi import status
# from fastapi_pagination import Params
# from fastapi_pagination.ext.sqlalchemy import paginate


class PatientUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def add_patient(self, patient: Patient):
        patient_model = PatientModel(**patient.dict())
        self.db_session.add(patient_model)
        self.db_session.commit()

    def list_patients(self):
        patients_on_db = self.db_session.query(PatientModel).all()
        patient_output = [
            self.serialize_patient(patient_model)
            for patient_model in patients_on_db
        ]
        return patient_output
    
    def list_patients_by_id(self, id):
        result = {}
        patients_on_db = self.db_session.query(PatientModel).filter_by(id=id).first()

        uc = MeasurementUseCases()
        measurements_on_db = uc.list_measurements_by_patients_id(patient_id=id)

        person_dict = patients_on_db.to_dict()
        measurements_dict = measurements_on_db.to_dict()
        result.update(person_dict)
        result['measurements'] = measurements_dict
        
        return result
    
    def serialize_patient(self, patient_model: PatientModel):
        return PatientOutput(**patient_model.__dict__)
 
    # def serialize_patient(self, patient_model: patientModel):
    # def list_patients(self, page: int = 1, size: int = 50):
    #     patients_on_db = self.db_session.query(PatientModel)
    #     params = Params(page=page, size=size)
    #     return paginate(patients_on_db, params=params)

    def delete_patient(self, id):
        patient_model = self.db_session.query(PatientModel).filter_by(id=id).first()
        if not patient_model:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='patient not found')
        
        self.db_session.delete(patient_model)
        self.db_session.commit()

        return PatientOutput(**patient_model.__dict__)
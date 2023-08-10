from app.db.models import Measurement as MeasurementModel
from app.utils.format_helper import message_to_json
from app.db.connection import Session

class MeasurementUseCases:
    def __init__(self):
        self.db_session = Session()

    def add_patient_from_queue(self, measurement_message: str):
        measurement = message_to_json(data=measurement_message)
        print(measurement)
        measurement_model = MeasurementModel(**measurement)
        self.db_session.add(measurement_model)
        self.db_session.commit()

    
    def list_measurements_by_patients_id(self, patient_id):
        measurement_on_db = self.db_session.query(MeasurementModel).filter_by(patient_id=patient_id).first()
        return measurement_on_db
        # if patients_on_db is not None:
        #     patient_output = self.serialize_patient(patients_on_db)
        #     return patient_output
        # return None
    
    # def serialize_patient(self, patient_model: PatientModel):
    #     return PatientOutput(**patient_model.__dict__)
 

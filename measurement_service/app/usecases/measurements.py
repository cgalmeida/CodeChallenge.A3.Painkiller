from sqlalchemy.orm import Session
from app.db.models import Measurements as MeasurementModel
from app.schemas.measures import Measurement, MeasurementOutput
from fastapi.exceptions import HTTPException
from fastapi import status
# from fastapi_pagination import Params
# from fastapi_pagination.ext.sqlalchemy import paginate


class MeasurementUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def add_measure(self, measure: Measurement):
        measure_model = MeasurementModel(**measure.dict())
        self.db_session.add(measure_model)
        self.db_session.commit()

    def list_measures(self):
        measures_on_db = self.db_session.query(MeasurementModel).all()
        measure_output = [
            self.serialize_measure(measure_model)
            for measure_model in measures_on_db
        ]
        return measure_output
    
    def list_measures_by_id(self, id):
        measures_on_db = self.db_session.query(MeasurementModel).filter_by(id=id).first()
        return measures_on_db
    
    def list_measures_by_patient_id(self, patient_id):
        measures_on_db = self.db_session.query(MeasurementModel).filter_by(patient_id=patient_id)
        measure_output = [
                self.serialize_measure(measure_model)
                for measure_model in measures_on_db
            ]
        return measure_output
    
    def serialize_measure(self, measure_model: MeasurementModel):
        return MeasurementOutput(**measure_model.__dict__)
 
    # def serialize_measure(self, measure_model: MeasurementModel):
    # def list_measures(self, page: int = 1, size: int = 50):
    #     measures_on_db = self.db_session.query(MeasurementModel)
    #     params = Params(page=page, size=size)
    #     return paginate(measures_on_db, params=params)

    def delete_measure(self, id):
        measure_model = self.db_session.query(MeasurementModel).filter_by(id=id).first()
        if not measure_model:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='measure not found')
        
        self.db_session.delete(measure_model)
        self.db_session.commit()

        return MeasurementOutput(**measure_model.__dict__)
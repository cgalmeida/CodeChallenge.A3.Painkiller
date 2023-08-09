from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, Response, status, Body
from sqlalchemy.orm import Session
from app.schemas.measures import Measurement, MeasurementOutput
from app.usecases.measurements import MeasurementUseCases
from app.usecases.queue_message import QueueMessageUseCases 
from app.routes.deps import get_db_session


router = APIRouter(prefix='/api/v1/measures', tags=['Measures'])

@router.post('/', status_code=status.HTTP_201_CREATED, 
             description="Receive a new measures's data (name, age, medical conditions, etc.) in JSON format, store it in a database, and return the measures object with an assigned ID.")
async def add_measures(
    measure: Measurement,
    db_session: Session = Depends(get_db_session)
):
    uc = MeasurementUseCases(db_session=db_session)
    uc.add_measure(measure=measure)
    
    qm = QueueMessageUseCases()
    # Serializing the object into a binary string
    message=str(measure)
    await qm.send_message(message)

    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/list', response_model=List[MeasurementOutput], 
            description="Return a paginated list with data of all measures")
def list_measures(
    db_session: Session = Depends(get_db_session)
):
    uc = MeasurementUseCases(db_session=db_session)
    response = uc.list_measures()
    
    return response

@router.get('/list/{id}', 
            description="Return the data of the measures corresponding to the measures_id.")
def list_measures_by_id(
    id,
    db_session: Session = Depends(get_db_session)
):
    uc = MeasurementUseCases(db_session=db_session)
    response = uc.list_measures_by_id(id=id)
    
    return response

@router.get('/{patient_id}/list/', 
            description="Return the data of the measures corresponding to the measures_id.")
def list_measures_by_id(
    patient_id,
    db_session: Session = Depends(get_db_session)
):
    uc = MeasurementUseCases(db_session=db_session)
    response = uc.list_measures_by_patient_id(patient_id=patient_id)
    
    return response

@router.delete('/delete/{id}', 
               description="Deletes the data of the measures corresponding to the measures_id.")
def delete_measures(
    id,
    db_session: Session = Depends(get_db_session)
):
    uc = MeasurementUseCases(db_session=db_session)
    uc.delete_measure(id=id)
    
    return Response(status_code=status.HTTP_200_OK)

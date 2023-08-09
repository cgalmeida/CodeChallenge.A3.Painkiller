from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, Response, status, Body
from sqlalchemy.orm import Session
from app.schemas.patient import Patient, PatientOutput
from app.usecases.patient import PatientUseCases
from app.usecases.queue_message import QueueMessageUseCases
from app.routes.deps import get_db_session


router = APIRouter(prefix='/api/v1/patient', tags=['Patient'])

@router.post('/', status_code=status.HTTP_201_CREATED, 
             description="Receive a new patient's data (name, age, medical conditions, etc.) in JSON format, store it in a database, and return the patient object with an assigned ID.")
def add_patient(
    patient: Patient,
    db_session: Session = Depends(get_db_session)
):
    uc = PatientUseCases(db_session=db_session)
    uc.add_patient(patient=patient)
    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/list', response_model=List[PatientOutput], 
            description="Return list with data of all patient")
def list_patient(
    db_session: Session = Depends(get_db_session)
):
    uc = PatientUseCases(db_session=db_session)
    response = uc.list_patients()
    
    return response

@router.get('/{id}', 
            description="Return the data of the patient corresponding to the patient_id.")
def list_patient_by_id(
    id,
    db_session: Session = Depends(get_db_session)
):
    uc = PatientUseCases(db_session=db_session)
    response = uc.list_patients_by_id(id=id)
    
    return response

@router.delete('/delete/{id}', 
               description="Deletes the data of the patient corresponding to the patient_id.")
def delete_patient(
    id,
    db_session: Session = Depends(get_db_session)
):
    uc = PatientUseCases(db_session=db_session)
    uc.delete_patient(id=id)
    
    return Response(status_code=status.HTTP_200_OK)

@router.post("/send")
async def send_message(message: str = Body(..., embed=True)):
    print("do something...")
    qm = QueueMessageUseCases()
    resp = await qm.send_message(message)
    return resp


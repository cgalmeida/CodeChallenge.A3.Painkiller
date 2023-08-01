from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.schemas.patient import Patient, PatientOutput
from app.usecases.patient import PatientUseCases
from app.routes.deps import get_db_session

router = APIRouter(prefix='/patient', tags=['Patient'])

@router.post('/add', status_code=status.HTTP_201_CREATED, description="Add new patient")
def add_patient(
    patient: Patient,
    db_session: Session = Depends(get_db_session)
):
    uc = PatientUseCases(db_session=db_session)
    uc.add_patient(patient=patient)
    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/list', response_model=List[PatientOutput])
def list_patient(
    db_session: Session = Depends(get_db_session)
):
    uc = PatientUseCases(db_session=db_session)
    response = uc.list_patients()
    
    return response

@router.delete('/delete/{id}', description='delete')
def delete_patient(
    id,
    db_session: Session = Depends(get_db_session)
):
    uc = PatientUseCases(db_session=db_session)
    uc.delete_patient(id=id)
    
    return Response(status_code=status.HTTP_200_OK)


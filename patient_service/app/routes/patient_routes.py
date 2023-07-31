from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.schemas.patient import Patient
from app.usecases.patient import PatientUseCases
from app.routes.deps import get_db_session

router = APIRouter(prefix='/patient', tags=['Patient'])

@router.post('/add')
def add_patient(
    patient: Patient,
    db_session: Session = Depends(get_db_session)
):
    uc = PatientUseCases(db_session=db_session)
    uc.add_patient(patient=patient)
    return Response(status_code=status.HTTP_201_CREATED)
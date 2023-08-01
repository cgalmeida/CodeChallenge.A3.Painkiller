import pytest
from app.usecases.patient import PatientUseCases
from app.db.models import Patient as PatientModel
from app.schemas.patient import Patient, PatientOutput
from fastapi.exceptions import HTTPException
# from fastapi_pagination import Page


def test_add_patient_uc(db_session):
    uc = PatientUseCases(db_session)
    
    patient = Patient(
        first_name= 'John',
        last_name= 'Doe',
        age= 55,
        condition= 'Healthy'
    )

    uc.add_patient(patient=patient)

    patients_on_db = db_session.query(PatientModel).all()
    
    #assert len(patients_on_db) == 1
    assert patients_on_db[0].first_name == 'John'
    assert patients_on_db[0].condition == 'Healthy'

    db_session.delete(patients_on_db[0])
    db_session.commit()


def test_list_patients_uc(db_session, patients_on_db):
    uc = PatientUseCases(db_session=db_session)

    patients = uc.list_patients()

    #assert len(patients) == 5
    assert type(patients[0]) == PatientOutput
    assert patients[0].first_name== patients_on_db[0].first_name
    assert patients[0].last_name== patients_on_db[0].last_name
    assert patients[0].age== patients_on_db[0].age
    assert patients[0].condition== patients_on_db[0].condition


def test_delete_patient(db_session):
    patient_model = PatientModel(first_name='John', last_name='Doe', age=55, condition='Healthy')
    db_session.add(patient_model)
    db_session.commit()

    uc = PatientUseCases(db_session=db_session)
    uc.delete_patient(id=patient_model.id)

    patient_model = db_session.query(PatientModel).first()
    assert patient_model is None


def test_delete_patient_non_exist(db_session):
    uc = PatientUseCases(db_session=db_session)
    with pytest.raises(HTTPException):
        uc.delete_patient(id='11111111-1111-1111-1111-111111111111')
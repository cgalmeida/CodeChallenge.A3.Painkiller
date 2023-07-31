import pytest
from app.usecases.patient import PatientUseCases
from app.db.models import Patient as PatientModel
from app.schemas.patient import Patient
# from fastapi.exceptions import HTTPException
# from fastapi_pagination import Page


def test_add_patient_uc(db_session):
    uc = PatientUseCases(db_session)
    
    patient = Patient(
        first_name= 'John',
        last_name= 'Doe',
        age= 16,
        condition= 'none'
    )

    uc.add_patient(patient=patient)

    patients_on_db = db_session.query(PatientModel).all()
    
    # assert len(patients_on_db) == 1
    assert patients_on_db[0].first_name == 'John'
    assert patients_on_db[0].condition == 'none'

    db_session.delete(patients_on_db[0])
    db_session.commit()


def test_list_patients_uc(db_session, patients_on_db):
    uc = patientUseCases(db_session=db_session)

    page = uc.list_patients(page=1, size=2)

    assert type(page) == Page
    assert len(page.items) == 2
    assert page.total == 4
    assert page.page == 1
    assert page.size == 2
    assert page.pages == 2


# def test_delete_patient(db_session):
#     patient_model = patientModel(name='Roupa', slug='roupa')
#     db_session.add(patient_model)
#     db_session.commit()

#     uc = patientUseCases(db_session=db_session)
#     uc.delete_patient(id=patient_model.id)

#     patient_model = db_session.query(patientModel).first()
#     assert patient_model is None


# def test_delete_patient_non_exist(db_session):
#     uc = patientUseCases(db_session=db_session)
#     with pytest.raises(HTTPException):
#         uc.delete_patient(id=1)
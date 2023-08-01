from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Patient as PatientModel
from app.main import app

client = TestClient(app)

def test_add_patient_route(db_session):
    body = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 55,
        "condition": "Healthy",     
    }

    response = client.post('/patient/add', json=body)

    assert response.status_code == status.HTTP_201_CREATED

    patients_on_db = db_session.query(PatientModel).all()
    
    # assert len(patients_on_db) == 1
    db_session.delete(patients_on_db[0])
    db_session.commit()

def test_list_patient_route(patients_on_db):
    response = client.get('/patient/list')

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert len(patients_on_db) == 5
    assert data[0]['first_name'] == patients_on_db[0].first_name
    assert data[0]['last_name'] == patients_on_db[0].last_name
    assert data[0]['age'] == patients_on_db[0].age
    assert data[0]['condition'] == patients_on_db[0].condition

def test_delete_patient_route(db_session):
    patient_model = PatientModel(first_name='John', last_name='Doe', age=55, condition='Healthy')
    db_session.add(patient_model)
    db_session.commit()

    response = client.delete(f'/patient/delete/{patient_model.id}')

    assert response.status_code == status.HTTP_200_OK

    patient_model = db_session.query(PatientModel).first()
    assert patient_model is None

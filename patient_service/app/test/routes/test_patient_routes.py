from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Patient as PatientModel
from app.main import app

client = TestClient(app)

def test_add_patient_route(db_session):
    body = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 16,
        "condition": "none",     
    }

    response = client.post('/patient/add', json=body)

    assert response.status_code == status.HTTP_201_CREATED

    patients_on_db = db_session.query(PatientModel).all()
    #TODO:fix delete tests on db
    #assert len(patients_on_db) == 1
    db_session.delete(patients_on_db[0])
    db_session.commit()

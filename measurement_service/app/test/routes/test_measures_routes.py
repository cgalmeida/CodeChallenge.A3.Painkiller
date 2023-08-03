from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Measurements as MeasurementModel
from app.main import app

client = TestClient(app)

def test_add_measure_route(db_session):
    body = {
        "temperature_celsius": 36.5,
        "blood_pressure_sys": 120,
        "blood_pressure_dias": 80,
        "body_weight": 60,
        "height_cm": 165,
        "stroke": False,
        "diabetes": False  , 
        "patient_id": "2982f106-0ecc-4f58-8f27-c463f6e9018b"
    }

    response = client.post('http://localhost:8081/api/v1/measures', json=body)

    assert response.status_code == status.HTTP_201_CREATED

    measures_on_db = db_session.query(MeasurementModel).all()
    
    # assert len(measures_on_db) == 1
    db_session.delete(measures_on_db[0])
    db_session.commit()

# def test_list_measure_route(measures_on_db):
#     response = client.get('/api/v1/measure/list')

#     assert response.status_code == status.HTTP_200_OK
#     data = response.json()

#     assert len(measures_on_db) == 5
#     assert data[0]['first_name'] == measures_on_db[0].first_name
#     assert data[0]['last_name'] == measures_on_db[0].last_name
#     assert data[0]['age'] == measures_on_db[0].age
#     assert data[0]['condition'] == measures_on_db[0].condition

# def test_delete_measure_route(db_session):
#     measure_model = MeasurementModel(first_name='John', last_name='Doe', age=55, condition='Healthy')
#     db_session.add(measure_model)
#     db_session.commit()

#     response = client.delete(f'/api/v1/measure/delete/{measure_model.id}')

#     assert response.status_code == status.HTTP_200_OK

#     measure_model = db_session.query(MeasurementModel).first()
#     assert measure_model is None

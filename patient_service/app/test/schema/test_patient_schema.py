import pytest
from app.schemas.patient import Patient

def test_patient_schema():
    patient = Patient(
        first_name='John',
        last_name='Doe',
        age=65,
        condition='pain'
    )
    
    assert patient.dict() == {
        'first_name':'John',
        'last_name':'Doe',
        'age':65,
        'condition':'pain'
    }

def test_patient_schema_invalid_age():
    with pytest.raises(ValueError):
        patient = Patient(
            first_name='John',
            last_name='Doe',
            age=165,
            condition='pain'
        )
    
    with pytest.raises(ValueError):
        patient = Patient(
            first_name='John',
            last_name='Doe',
            age=-4,
            condition='pain'
        )

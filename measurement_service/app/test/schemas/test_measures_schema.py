import pytest
from app.schemas.measures import Measurement

def test_maeasure_schema():
    maeasure = Measurement(
        first_name='John',
        last_name='Doe',
        age=65,
        condition='pain'
    )
    
    assert maeasure.dict() == {
        'first_name':'John',
        'last_name':'Doe',
        'age':65,
        'condition':'pain'
    }

def test_maeasure_schema_invalid_age():
    with pytest.raises(ValueError):
        maeasure = Measurement(
            first_name='John',
            last_name='Doe',
            age=165,
            condition='pain'
        )
    
    with pytest.raises(ValueError):
        maeasure = Measurement(
            first_name='John',
            last_name='Doe',
            age=-4,
            condition='pain'
        )

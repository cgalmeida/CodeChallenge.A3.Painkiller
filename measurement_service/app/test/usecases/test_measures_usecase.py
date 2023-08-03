import pytest
from app.usecases.measurements import MeasurementUseCases
from app.db.models import Measurements as MeasureModel
from app.schemas.measures import Measurement, MeasurementOutput
from fastapi.exceptions import HTTPException
# from fastapi_pagination import Page


def test_add_measure_uc(db_session):
    uc = MeasurementUseCases(db_session)
    
    measure = Measurement(
        first_name= 'John',
        last_name= 'Doe',
        age= 55,
        condition= 'Healthy'
    )

    uc.add_measure(measure=measure)

    measures_on_db = db_session.query(MeasureModel).all()
    
    #assert len(measures_on_db) == 1
    assert measures_on_db[0].first_name == 'John'
    assert measures_on_db[0].condition == 'Healthy'

    db_session.delete(measures_on_db[0])
    db_session.commit()


def test_list_measures_uc(db_session, measures_on_db):
    uc = MeasurementUseCases(db_session=db_session)

    measures = uc.list_measures()

    #assert len(measures) == 5
    assert type(measures[0]) == MeasurementOutput
    assert measures[0].first_name== measures_on_db[0].first_name
    assert measures[0].last_name== measures_on_db[0].last_name
    assert measures[0].age== measures_on_db[0].age
    assert measures[0].condition== measures_on_db[0].condition


def test_delete_measure(db_session):
    measure_model = MeasureModel(first_name='John', last_name='Doe', age=55, condition='Healthy')
    db_session.add(measure_model)
    db_session.commit()

    uc = MeasurementUseCases(db_session=db_session)
    uc.delete_measure(id=measure_model.id)

    measure_model = db_session.query(MeasureModel).first()
    assert measure_model is None


def test_delete_measure_non_exist(db_session):
    uc = MeasurementUseCases(db_session=db_session)
    with pytest.raises(HTTPException):
        uc.delete_measure(id='11111111-1111-1111-1111-111111111111')
from sqlalchemy import inspect

def assert_model_fields(model, expected_fields):
    columns = set(inspect(model).columns.keys())
    assert columns == set(expected_fields)

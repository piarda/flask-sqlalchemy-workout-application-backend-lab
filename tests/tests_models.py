# tests/test_models.py

from server.schemas import ExerciseSchema
from marshmallow import ValidationError

def test_exercise_schema_validation():
    schema = ExerciseSchema()

    valid_data = {"name": "Push Up", "category": "strength"}
    loaded = schema.load(valid_data)
    assert loaded.name == "Push Up"

    invalid_data = {"name": "Pu", "category": "unknown"}

    try:
        schema.load(invalid_data)
        assert False
    except ValidationError as err:
        assert "name" in err.messages or "category" in err.messages

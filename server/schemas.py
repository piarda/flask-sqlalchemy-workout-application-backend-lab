# server/schemas.py

from flask_marshmallow import Marshmallow
from marshmallow import validates, ValidationError, validates_schema
from marshmallow import fields
from marshmallow.validate import Length, OneOf, Range
from server.models import Exercise, Workout, WorkoutExercise

ma = Marshmallow()

class ExerciseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Exercise
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field(required=True, validate=Length(min=3))
    category = ma.auto_field(required=True, validate=OneOf(["strength", "cardio", "flexibility"]))
    equipment_needed = ma.auto_field()

class WorkoutExerciseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True

    id = ma.auto_field()
    workout_id = ma.auto_field()
    exercise_id = ma.auto_field()
    reps = ma.auto_field(validate=Range(min=1))
    sets = ma.auto_field(validate=Range(min=1))
    duration_seconds = ma.auto_field(validate=Range(min=1))

class WorkoutSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Workout
        load_instance = True
    
    id = ma.auto_field()
    date = fields.Date(required=True)
    duration_minutes = ma.auto_field(required=True, validate=Range(min=1))
    notes = ma.auto_field(validate=Length(max=500))

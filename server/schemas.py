# server/schemas.py

from flask_marshmallow import Marshmallow
from server.models import Exercise, Workout, WorkoutExercise

ma = Marshmallow()

class ExerciseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Exercise
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
    category = ma.auto_field()
    equipment_needed = ma.auto_field()

class WorkoutExerciseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True

    id = ma.auto_field()
    workout_id = ma.auto_field()
    exercise_id = ma.auto_field()
    reps = ma.auto_field()
    sets = ma.auto_field()
    duration_seconds = ma.auto_field()

class WorkoutSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Workout
        load_instance = True
    
    id = ma.auto_field()
    date = ma.auto_field()
    duration_minutes = ma.auto_field()
    notes = ma.auto_field()

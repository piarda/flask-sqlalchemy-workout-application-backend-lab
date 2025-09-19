from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Exercise(db.Model):
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80))
    equipment_needed = db.Column(db.Boolean, default=False)

    # One-to-many relationship with WorkoutExercise
    workout_exercises = db.relationship('WorkoutExercise', backref='exercise', lazy=True)

    # Many-to-many relationship with Workout (Exercise has many Workouts through WorkoutExercises)
    workouts = db.relationship('Workout', secondary='workout_exercise', backref='exercises', lazy=True)

    def __repr__(self):
        return f"<Exercise {self.name}>"
    
class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    # One-to-many relationship with WorkoutExercise
    workout_exercises = db.relationship('WorkoutExercise', backref='workout', lazy=True)

    # Many-to-many relationship with Exercise (Workout has many Exercises through WorkoutExercises)
    exercises = db.relationship('Exercise', secondary='workout_exercise', backref='workouts', lazy=True)

    def __repr__(self):
        return f"<Workout {self.id} - {self.date}>"
    
class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercise'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    def __repr__(self):
        return f"<WorkoutExercise {self.workout_id} - {self.exercise_id}>"


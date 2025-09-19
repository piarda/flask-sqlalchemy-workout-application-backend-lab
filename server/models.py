from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import datetime

db = SQLAlchemy()

class Exercise(db.Model):
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    category = db.Column(db.String(80))
    equipment_needed = db.Column(db.Boolean, default=False)

    # One-to-many relationship with WorkoutExercise
    workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise', cascade="all, delete-orphan", overlaps="workouts")

    # Many-to-many relationship with Workout through WorkoutExercise
    workouts = db.relationship('Workout', secondary='workout_exercise', back_populates='exercises', overlaps="workout_exercises")

    # Length of name for Exercise validation
    @validates('name')
    def validate_name(self, key, value):
        if len(value) < 3:
            raise ValueError("Exercise name must be at least 3 characters long")
        return value
    
    def __repr__(self):
        return f"<Exercise {self.name}>"
    

class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    # One-to-many relationship with WorkoutExercise
    workout_exercises = db.relationship('WorkoutExercise', back_populates="workout", cascade="all, delete-orphan", overlaps="exercises")

    # Many-to-many relationship with Exercise through WorkoutExercise
    exercises = db.relationship('Exercise', secondary='workout_exercise', back_populates="workouts", overlaps="workout_exercises")
    
    # Table constraint ensuring the duration_minutes is more than 0
    __table_args__ = (
        db.CheckConstraint('duration_minutes > 0', name='check_duration_minutes'),
    )

    # Validation for duration_minutes
    @validates('duration_minutes')
    def validate_duration(self, key, value):
        if value <= 0:
            raise ValueError("Duration minutes must be greater than zero")
        return value

    # Validation for date being either past or present
    @validates('date')
    def validate_date(self, key, value):
        if value > datetime.today().date():
            raise ValueError("Workout date cannot be in the future")
        return value
    
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

    # One-to-many foreign key relationships
    workout = db.relationship("Workout", back_populates="workout_exercises", overlaps="exercises,workouts")
    exercise = db.relationship("Exercise", back_populates="workout_exercises", overlaps="exercises,workouts")

    # Table constraint to ensure reps, sets, and duration_seconds are not negative
    __table_args__ = (
        db.CheckConstraint('reps >= 0', name='check_reps_positive'),
        db.CheckConstraint('sets >= 0', name='check_sets_positive'),
        db.CheckConstraint('duration_seconds >= 0', name='check_duration_seconds_positive'),
    )

    # Validation for reps, sets, and duration_seconds
    @validates('reps', 'sets', 'duration_seconds')
    def validate_non_negative(self, key, value):
        if value < 0:
            raise ValueError(f"{key} must not be negative")
        return value

    def __repr__(self):
        return f"<WorkoutExercise {self.workout_id} - {self.exercise_id}>"

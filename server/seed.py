#!/usr/bin/env python3

from server.app import app
from server.models import db, Exercise, Workout, WorkoutExercise
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed Exercises
    exercise1 = Exercise(name="Push Up", category="Bodyweight", equipment_needed=False)
    exercise2 = Exercise(name="Squat", category="Bodyweight", equipment_needed=False)
    exercise3 = Exercise(name="Deadlift", category="Strength", equipment_needed=True)
    db.session.add_all([exercise1, exercise2, exercise3])

    # Seed Workouts
    workout1 = Workout(date=date(2025, 9, 16), duration_minutes=30, notes="Morning strength class")
    workout2 = Workout(date=date(2025, 9, 18), duration_minutes=45, notes="Cardio and legs")
    db.session.add_all([workout1, workout2])

    # Adding Exercises to Workouts via WorkoutExercise
    workout_exercise1 = WorkoutExercise(workout=workout1, exercise=exercise1, reps=15, sets=3, duration_seconds=0)
    workout_exercise2 = WorkoutExercise(workout=workout1, exercise=exercise2, reps=20, sets=3, duration_seconds=0)
    workout_exercise3 = WorkoutExercise(workout=workout2, exercise=exercise3, reps=5, sets=3, duration_seconds=0)
    workout_exercise4 = WorkoutExercise(workout=workout2, exercise=exercise2, reps=25, sets=3, duration_seconds=0)
    db.session.add_all([workout_exercise1, workout_exercise2, workout_exercise3, workout_exercise4])

    db.session.commit()

    print("Seeding complete!")

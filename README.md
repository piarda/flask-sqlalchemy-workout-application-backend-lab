# Flask SQLAlchemy Workout Application Backend

This is a backend API for tracking workouts and exercises built with Flask, SQLAlchemy, and Marshmallow. It allows users to manage workouts and exercises through CRUD operations, leveraging SQLAlchemy as the ORM for database interactions. Additionally, users can associate exercises with specific workouts, enabling efficient tracking and management of workout data.


## Features:
- Workout Management: Create, read, and delete workouts.
- Exercise Management: Create, read, and delete exercises.
- Associating Exercises with Workouts: Add exercises to workouts.


## Technologies Used:
- Flask
- SQLAlchemy (An ORM (Object Relational Mapper) for Python to interact with the database)
- Flask-SQLAlchemy
- Flask-Marshmallow (Integration between Flask and Marshmallow for object serialization)
- pytest


## Installation & Running the App: 
1. Upon cloning the respository from GitHub, set up a virtual environment via:
        python3 -m venv venv
2. Install pipenv if you don't have it already:
        pip install pipenv
3. Install the required dependencies using pipenv:
        pipenv install
4. To activate the virtual environment, run:
        pipenv shell
5. Initialize the database and seed it with initial data:
        python -m server.seed
6. Start the Flask development server via:
        flask run
The app will run on http://localhost:5000


## API Endpoints:
Workouts:
- GET /workouts                 (Retrieve all workouts)
- GET /workouts/int:id          (Retrieve a specific workout by ID)
- POST /workouts                (Create a new workout)
        Example:
        {
          "date": "2025-09-20",
          "duration_minutes": 60,
          "notes": "Test workout"
        }
- DELETE /workouts/int:id       (Delete a specific workout by ID)

Exercises:
- GET /exercises                (Retrieve all exercises)
- GET /exercises/int:id         (Retrieve a specific exercise by ID)
- POST /exercises               (Create a new exercise)
        Example:
        {
          "name": "Test Exercise",
          "category": "strength",
          "equipment_needed": false
        }
- DELETE /exercises/int:id      (Delete a specific exercise by ID)

Add Exercise to Workout:
- POST /workouts/int:workout_id/exercises/int:exercise_id/workout_exercises             (Add an exercise to a workout)


## Testing:
Run the tests for the app via:
        python -m pytest
This will execute the test suite and provide a summary of the results.


Enjoy!
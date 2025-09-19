# tests/test_app.py

import json
from datetime import date

def test_get_workouts(client):
    response = client.get('/workouts')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_create_workout(client):
    workout_data = {
        "date": date.today().strftime("%Y-%m-%d"),  # Use today's date
        "duration_minutes": 60,
        "notes": "Test workout"
    }
    response = client.post('/workouts', data=json.dumps(workout_data),
                           content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert data['notes'] == "Test workout"
    assert "id" in data

def test_get_exercises(client):
    response = client.get('/exercises')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_create_exercise(client):
    exercise_data = {
        "name": "Test Exercise",
        "category": "strength",
        "equipment_needed": False
    }
    response = client.post('/exercises', data=json.dumps(exercise_data),
                           content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == "Test Exercise"
    assert "id" in data

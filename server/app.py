# server/app.py

from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from marshmallow import ValidationError
from server.models import db, Workout, Exercise, WorkoutExercise
from server.schemas import ma, WorkoutSchema, ExerciseSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)
ma.init_app(app)

#Reuseable schemas
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

# Workout Endpoints
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    result = workouts_schema.dump(workouts)
    return jsonify(result), 200

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    result = workout_schema.dump(workout)
    return jsonify(result), 200

@app.route('/workouts', methods=['POST'])
def create_workout():
    try:
        workout = workout_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    db.session.add(workout)
    db.session.commit()

    return workout_schema.jsonify(workout), 201

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return '', 204

# Exercise Endpoints
@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    result = exercises_schema.dump(exercises)
    return jsonify(result), 200

@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    result = exercise_schema.dump(exercise)
    return jsonify(result), 200

@app.route('/exercises', methods=['POST'])
def create_exercise():
    try:
        exercise = exercise_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    db.session.add(exercise)
    db.session.commit()

    return exercise_schema.jsonify(exercise), 201

@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    db.session.delete(exercise)
    db.session.commit()
    return '', 204

# Add Exercise to Workout
@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    return jsonify({"message": f"Add exercise {exercise_id} to workout {workout_id}"}), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)

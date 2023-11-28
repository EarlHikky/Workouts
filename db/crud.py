from datetime import datetime, timedelta

from pony.orm import db_session

import pydantic_models
from db import db
from models import User, Workout, WorkoutSet, Exercise

db.generate_mapping(create_tables=True)


@db_session
def create_user(name: str):
    User(name=name)


@db_session
def read_user(user_id: int):
    return User.get(id=user_id)


@db_session
def update_user(user_id: int, new_name: str):
    user = User.get(id=user_id)
    if not user:
        return None
    user.name = new_name
    return user


@db_session
def delete_user(user_id: int):
    user = User.get(id=user_id)
    if not user:
        return False
    user.delete()
    return True


@db_session
def create_workout(user: User):
    workout = Workout(date=datetime.now(), user=user)
    return workout


@db_session
def read_workout(workout_id: int):
    return Workout.get(id=workout_id)


@db_session
def update_workout(workout_id: int, new_date: datetime, new_duration: timedelta):
    workout = Workout.get(id=workout_id)
    if not workout:
        return None
    workout.date = new_date
    workout.duration = new_duration
    return workout


@db_session
def delete_workout(workout_id: int):
    workout = Workout.get(id=workout_id)
    if not workout:
        return False
    workout.delete()
    return True


@db_session
def get_workout_sets(workout_id: int):
    workout = Workout.get(id=workout_id)
    if not workout:
        return None
    return workout.sets


@db_session
def create_workout_set(workout: pydantic_models.Workout,
                       exercise: pydantic_models.Exercise):
    workout_set = WorkoutSet(workout=workout,
                             date=datetime.now(),
                             exercise=exercise)

    return workout_set


@db_session
def update_workout_set(workout_set: pydantic_models.WorkoutSet):
    set_to_update = WorkoutSet[workout_set.id]
    set_to_update.duration = workout_set.duration


@db_session
def create_exercise(title):
    exercise = Exercise(title=title)
    return exercise

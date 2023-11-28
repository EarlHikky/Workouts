import datetime

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
def create_workout(user: pydantic_models.User):
    current_user = User[1]
    # current_user = User[user.id]
    workout = Workout(date=datetime.datetime.now(),
                      user=current_user)
    return workout


def count_duration():
    start_time = datetime.datetime.now()
    workout_start_time = Workout[6].date
    previous_set_end_time = WorkoutSet[1]
    # previous_set = WorkoutSet.select(lambda ws: ws.workout == workout).order_by(WorkoutSet.date.desc()).first()
    return 1


@db_session
def create_workout_set(workout: pydantic_models.Workout,
                       exercise: pydantic_models.Exercise):
    workout_set = WorkoutSet(workout=workout,
                             date=datetime.datetime.now(),
                             exercise=exercise)

    return workout_set


@db_session
def update_workout_set(workout_set: pydantic_models.WorkoutSet):
    set_to_update = WorkoutSet[workout_set.id]
    set_to_update.duration = workout_set.duration
    duration = count_duration()


@db_session
def create_exercise(title):
    exercise = Exercise(title=title)
    return exercise

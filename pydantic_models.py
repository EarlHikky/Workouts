from datetime import datetime

import pydantic


# from db.models import Workout


class User(pydantic.BaseModel):
    id: int
    name: str = None
    workouts: 'Workout'


class Workout(pydantic.BaseModel):
    id: int
    date: datetime
    duration: datetime
    user: User


class WorkoutSet(pydantic.BaseModel):
    id: int
    workout: Workout
    date: datetime
    exercise: 'Exercise'
    duration: datetime
    weight: float
    rest: datetime
    reps: int


class Exercise(pydantic.BaseModel):
    id: int
    title: str
    set: WorkoutSet

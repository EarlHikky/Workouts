from datetime import datetime, timedelta

from pony.orm import *

db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    workouts = Set('Workout')


class Workout(db.Entity):
    id = PrimaryKey(int, auto=True)
    date = Optional(datetime)
    duration = Optional(timedelta)
    user = Required(User)
    sets = Set('Set')


class Set(db.Entity):
    id = PrimaryKey(int, auto=True)
    workout = Required(Workout)
    exercises = Required('Exercise')
    duration = Optional(timedelta)
    weight = Optional(float)
    rest = Optional(timedelta)
    reps = Optional(int)


class Exercise(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Optional(str)
    set = Optional(Set)


# db.generate_mapping()

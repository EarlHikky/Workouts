from datetime import datetime, timedelta

from pony.orm import Optional, Required, Set, set_sql_debug

from db import db


class User(db.Entity):
    name = Optional(str)
    workouts = Set('Workout')


class Workout(db.Entity):
    date = Optional(datetime)
    duration = Optional(timedelta)
    user = Required(User)
    sets = Set('WorkoutSet')


class WorkoutSet(db.Entity):
    workout = Required(Workout)
    date = Required(datetime)
    exercise = Required('Exercise')
    duration = Optional(timedelta)
    weight = Optional(float)
    rest = Optional(timedelta)
    reps = Optional(int)


class Exercise(db.Entity):
    title = Optional(str)
    sets = Set(WorkoutSet)


# db.generate_mapping()
set_sql_debug(True)
# db.generate_mapping(create_tables=True)

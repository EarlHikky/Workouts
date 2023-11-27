from models import *

db.bind(provider='sqlite', filename='workouts.sqlite', create_db=True)
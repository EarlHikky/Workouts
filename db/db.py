from pony.orm import Database

db = Database()
db.bind(provider='sqlite', filename='workouts.sqlite', create_db=True)
# db.generate_mapping(create_tables=True)
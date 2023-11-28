import threading
import time
from datetime import datetime, timedelta
from pony.orm import db_session, select, desc
from pydantic_models import WorkoutSet
from db.crud2 import UserManager, WorkoutManager, ExerciseManager


@db_session
def update_last_workout_set(workout_id, new_duration):
    # Выбираем последний тренировочный сет для конкретной тренировки
    last_workout_set = select(s for s in WorkoutSet if s.workout.id == workout_id).order_by(
        desc(lambda s: s.date)).limit(1)[:]

    # Если есть хотя бы один тренировочный сет, обновляем его
    if last_workout_set:
        last_workout_set = last_workout_set[0]  # Достаем объект из списка
        last_workout_set.duration = new_duration
        last_workout_set.reps = 15

        return True

    return False  # Если не найдено тренировочных сетов

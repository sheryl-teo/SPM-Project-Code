# from fastapi import APIRouter
# from config.db import conn
# from schemas.learning_journey import Learning_journey
# from models.learning_journey import learning_journeys
# from typing import List
# from sqlalchemy import func, select

# learning_journey = APIRouter()

# @learning_journey.get(
#     "/learning_journeys",
#     tags=["learning_journeys"],
#     response_model=List[Learning_journey],
#     description="Get a list of all learning journeys",
# )
# def get_users():
#     return conn.execute(learning_journeys.select()).fetchall()

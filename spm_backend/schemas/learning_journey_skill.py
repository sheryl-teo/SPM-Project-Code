from pydantic import BaseModel

class Learning_journey_skill(BaseModel):
    Learning_Journey_ID: str
    Skill_ID: str
    Obtained: int
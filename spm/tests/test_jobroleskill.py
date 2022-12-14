from fastapi import FastAPI
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_jobroleskill_1():
    """Happy Path
    """
    test_setup = client.post("/jobrole_skills/delete/hard",
            json = {
            "Job_Role_ID": "JR88", 
            "Skill_ID": "S88"
        }
    )

    response = client.post("/jobrole_skills/create",
        json = {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    )

    response = client.post("/skills/create",
        json = {
            "Skill_ID": "S88",
            "Skill_Name": "Test Skill 88",
            "Active": 1
        }
    )

    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR88",
            "Job_Role_Name": "Test Job Role 88",
            "Job_Department": "Chairman",
            "Active": 1
        }
    ]
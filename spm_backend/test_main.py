

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def testcreatejobrole():
    response = client.post(
        "/job_role/create_job_role",
        json={
            "Job_Role_ID": "JR111",
            "Job_Role_Name": "string",
            "Job_Department": "string"
            })
    assert response.status_code == 200
    assert response.json() == [
            {
                "Job_Role_ID": "JR111",
                "Job_Role_Name": "string",
                "Job_Department": "string"
            }
            ]
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_jobroleskill_1():
    """Happy Path
    """
    test_setup = client.post("/job_role_skills/delete/hard",
            json = {
            "Job_Role_ID": "JR1", 
            "Skill_ID": "S1"
        }
    )

    response = client.post("/job_role_skills/create",
        json = {
            "Job_Role_ID": "JR1",
            "Skill_ID": "S1",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR1",
            "Skill_ID": "S1",
            "Active": 1
        }
    ]

def test_create_jobroleskill_2():
    """Error: Job role ID does not exist
    """

    response = client.post(
        "/job_role_skills/create",
        json = {
            "Job_Role_ID": "JR99",
            "Skill_ID": "S1",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
      "Error_ID": "JR1",
      "Error_Desc": "The job role you're looking for is not inside our database. Check your search terms and try again.",
      "Error_Details": ""
            }
        ]
    }

def test_create_jobroleskill_3():
    """Error: Skill ID does not exist
    """

    response = client.post(
        "/job_role_skills/create",
        json = {
            "Job_Role_ID": "JR1",
            "Skill_ID": "S100",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
            "Error_ID": "S1",
            "Error_Desc": "The skill you're looking for is not inside our database. Check your search terms and try again.",
            "Error_Details": ""
            }
        ]
    }

def test_create_jobroleskill_4():
    """Error: Job role ID is not valid
    """

    response = client.post(
        "/job_role_skills/create",
        json = {
            "Job_Role_ID": "JS1",
            "Skill_ID": "S1",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
                "Error_ID": "JR1",
                "Error_Desc": "The job role you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            },
            {
                "Error_ID": "JR3",
                "Error_Desc": "This job role has an invalid job role ID. Check your job role ID and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_create_jobroleskill_5():
    """Error: Skill ID is not valid
    """

    response = client.post(
        "/job_role_skills/create",
        json = {
            "Job_Role_ID": "JR1",
            "Skill_ID": "T100",
            "Active": 1
        }
    )
    assert response.status_code == 200
    assert response.json() == {
    "errors": [
        {
            "Error_ID": "S1",
            "Error_Desc": "The skill you're looking for is not inside our database. Check your search terms and try again.",
            "Error_Details": ""
        },
        {
            "Error_ID": "S3",
            "Error_Desc": "This skill has an invalid skill ID. Check your skill ID and try again.",
            "Error_Details": ""
        }
    ]
}

def test_read_jobroleskill_jobrole_1():
    """Happy Path
    """

    response = client.get("/job_role_skills/read/jobrole/JR2")

    assert response.status_code == 200
    assert response.json() == {
        "S8": "Team management",
        "S16": "Communication",
        "S22": "Problem solving",
        "S21": "Decision making"
    }

def test_read_jobroleskill_jobrole_2():
    """Error: Job role does not exist
    """

    response = client.get("/job_role_skills/read/jobrole/JR100")

    assert response.status_code == 200
    assert response.json() == {
    "errors": [
            {
                "Error_ID": "JR1",
                "Error_Desc": "The job role you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_read_jobroleskill_jobrole_3():
    """Error: Job role ID is invalid
    """

    response = client.get("/job_role_skills/read/jobrole/JS1")

    assert response.status_code == 200
    assert response.json() == {
    "errors": [
            {
                "Error_ID": "JR1",
                "Error_Desc": "The job role you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            },
            {
                "Error_ID": "JR3",
                "Error_Desc": "This job role has an invalid job role ID. Check your job role ID and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_read_jobroleskill_skill_1():
    """Happy Path
    """

    response = client.get("/job_role_skills/read/skill/S8")

    assert response.status_code == 200
    assert response.json() == [
        {
            "Job_Role_ID": "JR2",
            "Skill_ID": "S8",
            "Active": 1
        }
    ]

def test_read_jobroleskill_skill_2():
    """Error: Job role does not exist
    """

    response = client.get("/job_role_skills/read/skill/S100")

    assert response.status_code == 200
    assert response.json() == {
    "errors": [
            {
                "Error_ID": "S1",
                "Error_Desc": "The skill you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_read_jobroleskill_skill_3():
    """Error: Job role ID is invalid
    """

    response = client.get("/job_role_skills/read/skill/T8")

    assert response.status_code == 200
    assert response.json() == {
    "errors": [
            {
                "Error_ID": "S1",
                "Error_Desc": "The skill you're looking for is not inside our database. Check your search terms and try again.",
                "Error_Details": ""
            },
            {
                "Error_ID": "S3",
                "Error_Desc": "This skill has an invalid skill ID. Check your skill ID and try again.",
                "Error_Details": ""
            }
        ]
    }

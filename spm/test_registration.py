from fastapi import FastAPI
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Read 

def test_read_registration_ID_1():
    """Happy Path: Read multiple registrations by staff ID
    """
    response = client.get("/registration/get_staff_completed_courses/130001")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Reg_ID": 1,
            "Course_ID": "COR002",
            "Staff_ID": 130001,
            "Reg_Status": "Registered",
            "Completion_Status": "Completed"
        },
        {
            "Reg_ID": 245,
            "Course_ID": "COR001",
            "Staff_ID": 130001,
            "Reg_Status": "Registered",
            "Completion_Status": "Completed"
        }
    ]

def test_read_registration_ID_2():
    """Happy Path: Read single registration by staff ID
    """
    response = client.get("/registration/get_staff_completed_courses/130002")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Reg_ID": 2,
            "Course_ID": "COR002",
            "Staff_ID": 130002,
            "Reg_Status": "Registered",
            "Completion_Status": "Completed"
        }
    ]
def test_read_registration_ID_3():
    """Valid Path: Staff does not exist
    """
    response = client.get("/registration/get_staff_completed_courses/999999")
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
            {
            "Error_ID": "R1",
            "Error_Desc": "This staff could not be found within the database. Check your staff ID and try again.",
            "Error_Details": ""
            }
        ]
    }

def test_read_registration_ID_4():
    """Error: Staff ID is too short
    """
    response = client.get("/registration/get_staff_completed_courses/9")
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
                {
                    "Error_ID": "S1",
                    "Error_Desc": "This staff has an invalid staff ID. Check your staff ID and try again.",
                    "Error_Details": ""
                },
                {
                    "Error_ID": "R1",
                    "Error_Desc": "This staff could not be found within the database. Check your staff ID and try again.",
                    "Error_Details": ""
                }
            ]
        }

def test_read_registration_ID_5():
    """Error: Staff ID is too short
    """
    response = client.get("/registration/get_staff_completed_courses/9999999")
    assert response.status_code == 200
    assert response.json() == {
        "errors": [
                {
                    "Error_ID": "S1",
                    "Error_Desc": "This staff has an invalid staff ID. Check your staff ID and try again.",
                    "Error_Details": ""
                },
                {
                    "Error_ID": "R1",
                    "Error_Desc": "This staff could not be found within the database. Check your staff ID and try again.",
                    "Error_Details": ""
                }
            ]
        }

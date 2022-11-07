from fastapi import FastAPI
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Read 

def test_read_staff_ID_1():
    """Happy Path: Read staff by staff ID
    """
    response = client.get("/staffs/get_staff_details/130001")
    assert response.status_code == 200
    assert response.json() == [
        {
            "Staff_ID": 130001,
            "Staff_FName": "John",
            "Staff_LName": "Sim",
            "Dept": "Chariman",
            "Email": "jack.sim@allinone.com.sg",
            "Role": 1
        }
    ]

def test_read_staff_ID_2():
    """Valid Path: Staff does not exist
    """
    response = client.get("/staffs/get_staff_details/999999")
    assert response.status_code == 200
    assert response.json() == [
    ]

def test_read_staff_ID_3():
    """Error: Staff ID is too short
    """
    response = client.get("/staffs/get_staff_details/9")
    assert response.status_code == 200
    assert response.json() == {
    "errors": [
            {
                "Error_ID": "S3",
                "Error_Desc": "This staff has an invalid staff ID. Check your staff ID and try again.",
                "Error_Details": ""
            }
        ]
    }

def test_read_staff_ID_4():
    """Error: Staff ID is too long
    """
    response = client.get("/staffs/get_staff_details/9999999999")
    assert response.status_code == 200
    assert response.json() == {
    "errors": [
            {
                "Error_ID": "S3",
                "Error_Desc": "This staff has an invalid staff ID. Check your staff ID and try again.",
                "Error_Details": ""
            }
        ]
    }

import requests
import pytest

@pytest.mark.positive
def test_createbooking_happypath():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type" : "application/json"}
    json_payload = {
        "firstname" : "Smith",
        "lastname" : "Allen",
        "totalprice" : 1000,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2024-01-01",
            "checkout" : "2024-01-05"
        },
        "additionalneeds" : "Lunch"
    }
    response = requests.post(url,headers=headers,json=json_payload)
    print(response.text)
    assert response.status_code==200, "booking creation error"
    data = response.json()
    bookingid= data["bookingid"]
    print(data["bookingid"])
    assert data["bookingid"] is not None, "booking is not created"
    assert data["booking"]["firstname"] == "Smith", "incorrect first name"
    print (type(headers))

@pytest.mark.negative
def test_create_booking_nopayload():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type" : "application/json"}
    json ={}
    response_payload = requests.post(url, headers=headers, json=json)
    assert response_payload.status_code == 500, "incorrect status code"
    assert response_payload.text == "Internal Server Error"

@pytest.mark.negative
def test_create_booking_noheader():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {}
    json = {
            "firstname": "Smith",
            "lastname": "Allen",
            "totalprice": 1000,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-01-05"
            },
            "additionalneeds": "Lunch"
        }
    response_payload = requests.post(url, headers=headers, json=json)
    assert response_payload.status_code == 500, "incorrect status code"
    assert response_payload.text=="Internal Server Error"

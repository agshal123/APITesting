import requests
import pytest

@pytest.mark.positive
def test_createtoken():
   url = "https://restful-booker.herokuapp.com/auth"
   headers = {"Content-Type" : "application/json"}
   json = {
    "username" : "admin",
    "password" : "password123"
        }
   response_payload = requests.post(url,headers=headers,json=json)
   data = response_payload.json()
   print(data)
   token = data["token"]
   assert 'token' in data,"token is not created"
@pytest.mark.negativetestcase
def test_invalidusername():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type" : "application/json"}
    json =  {
    "username" : "admin1",
    "password" : "password123"
        }
    response= requests.post(url,headers=headers,json=json)
    data = response.json()
    print(data)
    assert data["reason"]=="Bad credentials"

def createtoken():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json = {
        "username": "admin",
        "password": "password123"
        }
    response_payload = requests.post(url, headers=headers, json=json)
    data = response_payload.json()
    print(data)
    token = data["token"]
    return token

def createbookingid():
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
    return bookingid
@pytest.mark.positivetestcaseforPutRequest
def test_updatebooking():
   url="https://restful-booker.herokuapp.com/booking/"
   id=str(createbookingid())
   full_url = url+id
   cookie_value= "token="+createtoken()
   header={"Content-Type": "application/json",
           "Cookie" : cookie_value}
   print(header)
   json=    {
            "firstname" : "TestFirst1",
            "lastname" : "TestLast",
            "totalprice" : 1000,
            "depositpaid" : True,
            "bookingdates" : {
                "checkin" : "2024-01-01",
                "checkout" : "2024-01-05"
            },
            "additionalneeds" : "Dinner"
            }
   response=requests.put(full_url,headers=header,json=json)
   print(response)
   data = response.json()
   assert response.status_code==200,"not uodates"
   print(data)
   # assert data["firstname"]=="TestFirst"

@pytest.mark.deletepositivecase
def test_deletebooking():

        url = "https://restful-booker.herokuapp.com/booking"
        id = str(createbookingid())
        print(id)
        full_url=url+id
        cookie_value = "token=" + createtoken()
        headers = {"Content-Type": "application/json",
               "Cookie" : cookie_value}
        response= requests.delete(full_url,headers=headers)
        assert response.status_code==201, "booking not deleted"


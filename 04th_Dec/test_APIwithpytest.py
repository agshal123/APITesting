import pytest
import requests
import pytest_html

def test_getbookingid():
    url = "https://restful-booker.herokuapp.com/booking/"
    id = "1349"
    full_url = url  + id
    response_body = requests.get(full_url)
    # print (response_body.status_code)
    assert response_body.status_code==200, "id does not exist"
    print (response_body.json())
    data = response_body.json()
    assert 'firstname' in data, "firstname does not exist"
    assert data['firstname']=="Smith", "firstname is invalid"
    assert 'lastname' in data,"last name does not exist"
    assert data['lastname']=="Allen", "last name is invalid"
    assert data['bookingdates']['checkin']=="2024-01-01","invalid booking dates"




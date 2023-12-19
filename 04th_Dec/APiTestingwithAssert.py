import requests

# response_body = requests.get("https://restful-booker.herokuapp.com/booking/")
# print(response_body.text)
# print(response_body.headers)

#Test using Assert

def main():
    url = "https://restful-booker.herokuapp.com/booking"
    id = "2482"
    full_url= url+"/"+id
    print(full_url)
    response_body = requests.get(full_url)
    assert response_body.status_code==200,"id does not exist" # if sc!= 200 then error else no error
    data = response_body.json()
    print(data)
    assert 'firstname' in data, "first name key is not present"
    assert 'lastname' in data, "last name key is not present"
    assert data["firstname"]=="Josh","FirstName is not correct"
    assert data["lastname"] == "Allen", "LastName is not correct"
    assert data["bookingdates"]["checkin"]=="2018-01-01", "Incorrect booking dates"

if __name__=="__main__":
    main()
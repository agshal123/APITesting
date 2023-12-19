import requests

def main():
    response= requests.get("https://restful-booker.herokuapp.com/booking/")
    # print(response.status_code)
    print(response.json())
    # print(response.text)

    if response.status_code==200:
        print("TC#1 - Booking is fetched successfully")
    else:
        print("TC#1 - error")

if __name__=="__main__":
    main()
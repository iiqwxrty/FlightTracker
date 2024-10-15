# step 1: import requests
import requests
from dotenv import dotenv_values
dotenv = dotenv_values(".env")

# step 2: call api with given endpoint and key
response = requests.get("http://api.aviationstack.com/v1/flights?access_key="+dotenv["API_KEY"])
# step 3: convert to dictionary and grab only the "data" value
for i in response.json()["data"]:
    if i["flight_status"] == "active":
        print("Flight Airline: "+i["airline"]["name"])
        print("Flight Date: "+i["flight_date"])
        print("Flight Departure location: "+i["departure"]["airport"])
        print("Flight Arrival location: "+i["arrival"]["airport"])
        print("-----------------")

print(dotenv["api_key"])
# step 4: loop through the flights and check which flights are active

# step 5: if active, print the airline, date, departure airport and arrival airport HELLAO!
from pymongo import MongoClient
from pprint import pprint
import json

client = MongoClient(
    host='127.0.0.1',
    port=27017,
    username="root",
    password="root",
    authSource='admin'
)
st
#Getting the database instance
db = client["LufthansaDB"]


air_ports_dict={"Frankfurt Airport":"FRA",
            "Hamburg Airport":"HAM",
            "Düsseldorf International Airport":"DUS",
            "Heathrow Airport":"LHR",
            "London Luton Airport":"LTN",
            "Madrid–Barajas Airport":"MAD"
}

airport_col = db["airports"]
airport_col.drop()
airport_col.insert_one(air_ports_dict)

flights_col = db["flights"]
flights_col.drop()
flights_col.insert_one(air_ports_dict)



print(db.list_collection_names())

with open('../data/2022-11-28.json') as f:
    file_data = json.load(f)

# if pymongo < 3.0, use insert()
#mycol.insert_one(file_data)

"""cursor = mycol.find({})
for document in cursor:
    print(document)"""

pprint(list(airport_col.find()))
#print(mycol.get["FlightInformation"]["Flights"]["Flight"]["Departure"]["AirportCode"])

#results =list(mycol.find(filter={"FlightInformation.Flights.Flight.Arrival.AirportCode": "MAD","FlightInformation.Flights.Flight.Arrival.Actual.Time": "23:02"},projection={"Flight": 1, '_id': 0}))
#pprint(results)
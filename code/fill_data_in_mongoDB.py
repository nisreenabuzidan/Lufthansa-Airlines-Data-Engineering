#from pymongo import MongoClient
#from pprint import pprint
import json
import datetime
from get_countries import get_countries
from get_cities import get_cities
from get_airports import get_airports
from get_aircrafts import get_aircrafts
from get_customer_flight_information_on_route import get_customer_flight_information_on_route

def fill_reference_data_from_lufthansa_api(client, airports_list = [] , headers = {}):
    
        #Getting the database instance
        db = client["LufthansaDB"]
        
        #Fill in Countries info
        countries_col = db["countries"]
        countries_col.drop()


        cities_col = db["cities"]
        cities_col.drop()

        #Fill in Airports info
        airport_col = db["airports"]
        airport_col.drop()
        for airport_code in airports_list:
            airport_json = get_airports(airport_code,limit=100,LHoperated=0,headers=headers)
            if(airport_json):
                airport = airport_json["AirportResource"]["Airports"]["Airport"]
                airport_col.insert_one(airport)
                
                #get Countries related to Airports
                country_code = airport_json["AirportResource"]["Airports"]["Airport"]["CountryCode"]
                exist = countries_col.find_one(filter = {"CountryCode":country_code})
                if(exist==None):
                    countries_json = get_countries(country_code =country_code,headers=headers)
                    if(countries_json):
                        country = countries_json["CountryResource"]["Countries"]["Country"]
                        countries_col.insert_one(country)

                #get Cities related to Airports
                city_code = airport_json["AirportResource"]["Airports"]["Airport"]["CityCode"]
                exist = cities_col.find_one({"CityCode":city_code})
                if(exist==None):
                    cities_json = get_cities(city_code =city_code,headers=headers)
                    if(cities_json):
                        city = cities_json["CityResource"]["Cities"]["City"]
                        cities_col.insert_one(city)

        db_col = db.list_collection_names()
        output = '''
        ============================
        mongodb_db test
        ============================
        list_collection_names = {list_collection_names}
    
        '''


        with open('/logs/test_docker.log', 'a') as file:
            file.write(output.format(list_collection_names=db_col))

    

def fill_customer_flight_information_by_route(client,airports_list = [] ,date =datetime.datetime.now(), headers = {} ):
      
        #Fill in Aircrafts info
        aircrafts_col = db["aircrafts"]

        #Fill in customer_flight_information_by_route info
        col = db["flights"]

        for origin_airport_code in airports_list:
            for detination_airport_code in airports_list:
                if(origin_airport_code != detination_airport_code):
                    json_object = get_customer_flight_information_on_route(origin_airport_code,detination_airport_code,date,headers)
                    if(json_object):
                        for flight in json_object["FlightInformation"]["Flights"]["Flight"]:
                            col.insert_one(flight)
                            aircraft_code =flight["Equipment"]["AircraftCode"]
                            #get Aircfarts depending on Flight 
                            exist = aircrafts_col.find_one(filter = {"AircraftCode":aircraft_code})   
                            if(exist==None):
                                aircrafts_json= get_aircrafts(aircraft_code = aircraft_code,headers = headers)
                                if(aircrafts_json):
                                    aircraft = aircrafts_json["AircraftResource"]["AircraftSummaries"]["AircraftSummary"]
                                    aircrafts_col.insert_one(aircraft)
    
                            



"""i = 0 
cursor = col.find({})
for document in cursor:
    i = i+1
    print(document)

print(i)"""


#pprint(list(airport_col.find()))
#print(mycol.get["FlightInformation"]["Flights"]["Flight"]["Departure"]["AirportCode"])

#results =list(mycol.find(filter={"FlightInformation.Flights.Flight.Arrival.AirportCode": "MAD","FlightInformation.Flights.Flight.Arrival.Actual.Time": "23:02"},projection={"Flight": 1, '_id': 0}))
#pprint(results)
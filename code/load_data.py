from pymongo import MongoClient
from pprint import pprint
import json
import pandas as pd
from pandas import DataFrame

client = MongoClient(
    host='127.0.0.1',
    port=27017,
    username="root",
    password="root",
    authSource='admin'
)


db = client["LufthansaDB"]

#print(db.list_collection_names())


col = db["airports"]
cursor = col.find(projection=["AirportCode","Names","CountryCode","CityCode","Position"])
list_cur = list(cursor)
df_airports = DataFrame(list_cur)
#print(df_airports)

col = db["countries"]
cursor = col.find(projection=["CountryCode","Names"])
list_cur = list(cursor)
df_countries = DataFrame(list_cur)
#print(df_countries)

col = db["cities"]         
cursor = col.find()
list_cur = list(cursor)
df_cities = DataFrame(list_cur)
#print(df_cities)

col = db["aircrafts"]
cursor = col.find()
list_cur = list(cursor)
df_aircrafts = DataFrame(list_cur)
#print(df_aircrafts)



col = db["flights"]
cursor = col.find()
list_cur = list(cursor)
df_flights = DataFrame(list_cur)
#print(df_flights)

"""def calculate_latency():
    try:
        r = s.lookup_urls([url]) 
        return r.values()
    except:
        pass"""
#results =list(col.find(filter={"Arrival.AirportCode": "MAD","Scheduled.Date":"2022-12-02"},projection = {"Equipment.AircraftCode"}))

#pprint(results)

#print(df_flights["Departure"])#.Actual"}])
#feature3 = [d.get('Departure.Actual.DateTime') for d in df.dic]

"""feature3 = [d.get('Departure') for d in df_flights]
print(feature3)"""

my_list = df_flights["Departure"]
print(my_list)
my_list
#df_flights["latency_at_departure"] = df_flights["Departure.Actual.DateTime"] - df_flights["Departure.Scheduled.DateTime"]
#df_flights["latency_at_departure"]


"""cursor = col.find(filter={"Arrival.AirportCode": "MAD"},projection = {"Equipment.AircraftCode","Scheduled.Date"})
cursor = col.find(filter={"Arrival.AirportCode": "MAD","MarketingCarrierList.MarketingCarrier.FlightNumber":"6509","Departure.Scheduled.Date":"2022-12-01"})
"""







"""output = '''{cursor}
'''
from bson.json_util import dumps
json_data = dumps(list_cur)
#result_list = list_cur
with open('../logs/json_object.json', 'w') as file:
    #file.write(output.format(cursor=list(cursor)))
    json.dump(json_data, file,indent=4)"""

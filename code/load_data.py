from pymongo import MongoClient
from pprint import pprint
import json
import pandas as pd
from pandas import DataFrame
import datetime

client = MongoClient(
    host='127.0.0.1',
    port=27017,
    username="root",
    password="root",
    authSource='admin'
)


db = client["LufthansaDB"]


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



df_flights["departure_scheduled_dateTime"] = pd.to_datetime(df_flights["Departure"].str.get("Scheduled").str.get("Date")+" "+df_flights["Departure"].str.get("Scheduled").str.get("Time"))
df_flights["departure_actual_dateTime"] = pd.to_datetime(df_flights["Departure"].str.get("Actual").str.get("Date")+" "+df_flights["Departure"].str.get("Actual").str.get("Time"))
df_flights["arrival_scheduled_dateTime"] = pd.to_datetime(df_flights["Arrival"].str.get("Scheduled").str.get("Date")+" "+df_flights["Arrival"].str.get("Scheduled").str.get("Time"))
df_flights["arrival_actual_dateTime"] = pd.to_datetime(df_flights["Arrival"].str.get("Actual").str.get("Date")+" "+df_flights["Arrival"].str.get("Actual").str.get("Time"))


df_flights["latency_at_departure"] = df_flights["departure_actual_dateTime"] - df_flights["departure_scheduled_dateTime"]
df_flights["latency_at_arrival"] =df_flights["arrival_actual_dateTime"] - df_flights["arrival_scheduled_dateTime"]

print(df_flights[["departure_scheduled_dateTime","departure_actual_dateTime","latency_at_departure","arrival_scheduled_dateTime","arrival_actual_dateTime","latency_at_arrival"]])



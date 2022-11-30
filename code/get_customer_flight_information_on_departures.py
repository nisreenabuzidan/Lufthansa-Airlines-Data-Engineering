import datetime
import requests
import json 
import os
import pandas as pd

def get_customer_flight_information_on_departures(airport_code,departure_time=None,limit=50):
        if(departure_time==None):
            departure_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M").replace(' ','T')
            
        url = "https://api.lufthansa.com/v1/operations/customerflightinformation/departures/{airport_code}/{departure_time}/?limit={limit}".format(airport_code=airport_code,departure_time=departure_time,limit=limit)
        
        # sending get request and saving the response as response object
        r = requests.get(url = url, headers={"Authorization":"Bearer p5nz38jwntcz8fnb7qcjgjt5"})
        json_object= r.json()
        # Writing to json
        with open("../data/{departure_time}.json".format(departure_time=departure_time), "w") as outfile:
            json.dump(json_object, outfile,indent=4)
       


#get_customer_flight_information_on_departures("FRA","2022-11-30T07:00")


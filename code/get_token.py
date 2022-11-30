
import datetime
import requests
import json 
import os
import pandas as pd

client_id = "aqcu7jewgu2c785bvcvhm734"
client_secret = "MhXBQJBHnGrfqeJkxrMM"
grant_type = "client_credentials"


def get_access_token(client_id,client_secret,grant_type):
    # resquest
    url = "https://api.lufthansa.com/v1/oauth/token"
    params = { "client_id":client_id,
            "client_secret" : client_secret,
            "grant_type" : grant_type
    }
        
    # sending get request and saving the response as response object
    r = requests.post(url = url, data = params)
        
    # extracting data in json format
    token_respone = r.json()
    access_token = token_respone["access_token"]
    token_type =  token_respone["token_type"]

    
get_access_token()



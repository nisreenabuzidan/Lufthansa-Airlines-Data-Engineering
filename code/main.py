import os
from get_token import get_access_token


client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
grant_type = os.environ.get("GRANT_TYPE")


access_token_dict = get_access_token(client_id,client_secret,grant_type)

access_token = access_token_dict.get("access_token")
token_type = access_token_dict.get("token_type")

headers = {"Authorization":token_type+" "+access_token}


output = '''
============================
    get_access_token test
============================
 client_id = {client_id}
 client_secret = {client_secret}
 grant_type = {grant_type}
 access_token = {access_token}
 token_type = {token_type}
 headers = {headers}
 
'''


with open('/logs/test_docker.log', 'a') as file:
    file.write(output.format(client_id=client_id,client_secret=client_secret,grant_type=grant_type,access_token=access_token,token_type=token_type,headers=headers))
#import get_customer_flight_information_on_departures()
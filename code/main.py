import os
import datetime
from get_token import get_access_token
from pymongo import MongoClient
from fill_data_in_mongoDB import fill_reference_data_from_lufthansa_api
from fill_data_in_mongoDB import fill_customer_flight_information_by_route

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
grant_type = os.environ.get("GRANT_TYPE")


access_token_dict = get_access_token(client_id,client_secret,grant_type)

access_token = access_token_dict.get("access_token")
token_type = access_token_dict.get("token_type")

headers = {"Authorization":token_type+" "+access_token}


mongo_db_username = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
mongo_db_password = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
port = ""



mysql_db = os.environ.get("MYSQL_DATABASE")
mysql_db_password = os.environ.get("MYSQL_ROOT_PASSWORD")
port = ""

output = '''
============================
   mysqldb_connection test
============================
 current_time = {current_time}
 mysql_db = {mysql_db}
 mysql_db_password = {mysql_db_password}
 port = {port}

 
'''


with open('/logs/test_docker.log', 'a') as file:
    file.write(output.format(current_time=datetime.datetime.now(),mysql_db=mysql_db,mysql_db_password=mysql_db_password,port=port))



#Connect to Mongo DB Database
client = MongoClient(
    host='127.0.0.1',
    port=27017,
    username = mongo_db_username,
    password = mongo_db_password,
    authSource='admin',
    connectTimeoutMS=600000,
    socketTimeoutMS=600000,
    serverSelectionTimeoutMS=600000
)

output = '''
============================
   mongodb_connection test
============================
 current_time = {current_time}
 client = {client}
 

 
'''


with open('/logs/test_docker.log', 'a') as file:
    file.write(output.format(current_time=datetime.datetime.now(),client=client))

airports_list = ["FRA","HAM","LHR","LTN","MAD","CDG","DUS"]

#fill_reference_data_from_lufthansa_api(client,airports_list = airports_list ,headers = headers)

#date = "2022-12-01"
#fill_customer_flight_information_by_route(client,airports_list = airports_list ,date = date ,headers = headers)

#db = client["LufthansaDB"]
#print(db.list_collection_names())

#client.close()
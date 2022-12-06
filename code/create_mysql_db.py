
#from pymongo import MongoClient
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE lufthansadb")

#create table countries
sql ='''CREATE TABLE countries (
code VARCHAR(50) NOT NULL, 
name VARCHAR(100) NOT NULL, 
PRIMARY KEY (code)
)'''
mycursor.execute(sql)

#create table cities
sql = '''CREATE TABLE cities (
code VARCHAR(50) NOT NULL, 
name VARCHAR(100) NOT NULL, 
country_code VARCHAR(50) NOT NULL,
PRIMARY KEY (code),
FOREIGN KEY (country_code) REFERENCES countries(code)
)'''
mycursor.execute(sql)

#create table airports
sql = '''CREATE TABLE airports (
code VARCHAR(50) NOT NULL, 
name VARCHAR(100) NOT NULL, 
city_code VARCHAR(50) NOT NULL,
country_code VARCHAR(50) NOT NULL,
Latitude DECIMAL(5,5),
Longitude DECIMAL(5,5),
PRIMARY KEY (code),
FOREIGN KEY (country_code) REFERENCES countries(code),
FOREIGN KEY (city_code) REFERENCES cities(code)
)'''

mycursor.execute(sql)

#create table aircrafts
sql = '''CREATE TABLE aircrafts (
code VARCHAR(50) NOT NULL, 
name VARCHAR(100) NOT NULL, 
PRIMARY KEY (code)
)'''
mycursor.execute(sql)




sql = '''CREATE TABLE flights (
id INT AUTO_INCREMENT PRIMARY KEY,
departure_airport_code VARCHAR(50) NOT NULL, 
departure_scheduled_date DATETIME  NOT NULL, 
departure_scheduled_time DATETIME  NOT NULL, 
departure_actual_date DATETIME  NOT NULL, 
departure_actual_time DATETIME  NOT NULL, 
departure_terminal_name VARCHAR(100),
departure_terminal_gate VARCHAR(50),
departure_status_code VARCHAR(50),
departure_status_desc VARCHAR(100),

arrival_airport_code VARCHAR(50) NOT NULL,
arrival_scheduled_date DATETIME  NOT NULL, 
arrival_scheduled_time DATETIME  NOT NULL, 
arrival_actual_date DATETIME  NOT NULL, 
arrival_actual_time DATETIME  NOT NULL, 
arrival_terminal_name VARCHAR(100),
arrival_terminal_gate VARCHAR(50),
arrival_status_code VARCHAR(50),
arrival_status_desc VARCHAR(100),

flight_number VARCHAR(50) NOT NULL,
operating_carrier_airline_id VARCHAR(50) NOT NULL,
aircraft_code VARCHAR(50) NOT NULL,

FOREIGN KEY (aircraft_code) REFERENCES aircrafts(code)
)'''

mycursor.execute(sql)


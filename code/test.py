import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="lufthansadb"
)

mycursor = mydb.cursor()

sql =" insert into countries (code,name) values (%s, %s)"
val = ("fmf", "ff")
#mycursor.execute(sql,val)

mydb.commit()

"""print(mycursor.rowcount, "record inserted.")



sql =''' select * from countries
'''
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)"""

def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val

import  os, json

# read JSON file which is in the next parent folder
file = os.path.abspath('../data/json') + "/test.json"
json_data=open(file).read()
json_obj = json.loads(json_data)

for i, item in enumerate(json_obj):
    code = validate_string(item.get("code", None))
    name = validate_string(item.get("name", None))
    
    #mycursor.execute("INSERT INTO countries (code,name) VALUES (%s,%s)", (code,name))
mydb.commit()
#mydb.close()


sql =''' select * from countries
'''
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

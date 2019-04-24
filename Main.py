import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb+srv://testuser:987654321@cluster0-ndzg5.mongodb.net/test?retryWrites=true")
# db = client.admin

print(client.list_database_names())

dblist = client.list_database_names()
if "DRIVER" in dblist:
  print("The database exists.")

mydb = client["myTestDB"]
mycol = mydb["PhoneNumbers"]
mydict = ({'Name' : 'Neal', 'Phone Number' : 3019741074}, {'Name' : 'Gopal' , 'Phone Number' : 123456789})

myquery = {'Name' : 'Neal'}
if mycol.find(myquery):
    print('This entry has already been added to the collection.')
else:
    x = mycol.insert_many(mydict)
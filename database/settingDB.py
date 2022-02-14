# !/usr/bin/python3

from pymongo import MongoClient, errors
import subprocess
import json
db_name = ''
db_list = []
collections_list = []
collections_present = []
addresses = []

file = open('../json/DBConfig.json')
db_data = json.load(file)
file.close()

db_name = db_data['DBName']

for address in db_data['DBConfig']:
    add_server = str(address['server']) + ':' + str(address['port'])
    addresses.append(add_server)

for collection in db_data['DBCollection']:
    collections_list.append(str(collection))

client = MongoClient(host=addresses, ServerSelectionTimeoutMS=50, replicaset="rs0")

for db in client.list_database_names():
    db_list.append(str(db))

if db_name in db_list:
    for collection in client[db_name].collection_names():
        collections_present.append(str(collection))
else:
    client['DBName']

for collection_exist in collections_present:
    if collection_exist not in collections_list:
        client['DBName'][collection_exist]


print(collections_list, collections_present)
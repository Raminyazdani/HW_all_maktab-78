from pymongo import MongoClient
import bson
import os

file_name_database = "transactions_test"
file_name = "transaction.bson"
#   initializing Mongo client
client = MongoClient()

try:
    databases = client.list_database_names()
    if file_name_database not in databases:
        raise ValueError
    else:
        print(f"Database exists : {file_name_database}")
except ValueError:
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    if file_name in files:
        with open(file_name, 'rb') as f:
            data = bson.decode_all(f.read())
            try:
                x = os.system(f"mongorestore -d {file_name_database} {file_name}")
            except:
                print("Could not add data to database")
    else:
        print("failed to read transactions_test.bson")
except:
    print("failed to achieve connection to mongodb")

db = client.transactions_test
col = db.transaction
db_cache = client.transactions_test_cache
col_cache = db_cache.transaction

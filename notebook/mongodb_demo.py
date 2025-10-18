import pandas as pd
import pymongo


df = pd.read_csv('data.csv')
data = df.to_dict(orient='records')

DB_NAME = "Proj1"
COLLECTION_NAME = "Proj1-Data"
CONNECTION_URL = "mongodb+srv://eisashaiju_db_user:BJY9SION4viPNnN6@cluster0.ne28jiu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client=pymongo.MongoClient(CONNECTION_URL)
data_base=client[DB_NAME]
collection=data_base[COLLECTION_NAME]

rec=collection.insert_many(data)
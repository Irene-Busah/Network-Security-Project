import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from dotenv import load_dotenv



# loading the environment variable
load_dotenv('.env')

MONGO_DB_URL=os.getenv('MONGO_DB_URL')
print(MONGO_DB_URL)

# getting the certificate authority
ca=certifi.where()


# Implementing the data extraction class
class NetworkDataExtract():
    def __init__(self):
        try:
            pass

        except Exception as e:
            raise NetworkSecurityException(e, sys)
     
    # function to convert the csv data to json data
    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)

            records = list(json.loads(data.T.to_json()).values())

            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    # function to insert the data into the mongodb
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.records = records
            self.collection = collection

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]


            self.collection.insert_many(self.records)

            return len(self.records)
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    FILE_PATH = 'network_data/phisingData.csv'
    DATABASE = 'network_phishing'
    Collection = 'NetworkData'
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    num_of_records = networkobj.insert_data_mongodb(
        records=records,
        database=DATABASE,
        collection=Collection
    )
    print(num_of_records)


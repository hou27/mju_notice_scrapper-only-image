import os
import urllib3
# -*- coding: utf-8 -*-
from urllib.parse import quote
from pymongo import MongoClient
from dotenv import load_dotenv

SEARCH_STRING = '전과'

def save_to_db(data):
    print(data)
    load_dotenv(verbose=True)
    
    DB_PW = os.getenv('DB_PW')
    
    client = MongoClient("mongodb+srv://jalapeno:" + quote(DB_PW) + "@cluster211105.liaeo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    
    print(client.list_database_names())
    
    db = client['mju_notice']
    
    doc = {'search_value': SEARCH_STRING, 'data': data}
    
    db.notices.insert(doc)
    print(db.list_collection_names())
    
    return
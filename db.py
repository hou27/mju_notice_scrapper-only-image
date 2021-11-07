import os
import urllib3
# -*- coding: utf-8 -*-
import time
from urllib.parse import quote
from pymongo import MongoClient
from dotenv import load_dotenv

SEARCH_STRING = '전과'

def save_to_db(data):
    load_dotenv(verbose=True)
    
    created_at = time.strftime('%c', time.localtime(time.time()))
    
    DB_PW = os.getenv('DB_PW')
    
    client = MongoClient("mongodb+srv://jalapeno:" + quote(DB_PW) + "@cluster211105.liaeo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    
    db = client['mju_notice']
    
    doc = {'search_value': SEARCH_STRING, 'created_at': created_at, 'data': data}
    
    db.notices.insert(doc)
    
    return
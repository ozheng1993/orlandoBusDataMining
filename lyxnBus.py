#ou zheng
#2019/1/27
import requests
import numpy as np
import math
import os
from sys import argv
import shutil
import datetime
import csv
import json
import pandas as pd
from pandas.io.json import json_normalize
from datetime import datetime
import time
from IPython.display import clear_output
from pprint import pprint
#load lynx api
url = 'http://golynx.doublemap.com/map/v2/buses?key=aBcDeFgH'
start_time=datetime.now()
#create folder

def createFile():
    if os.path.exists('data'):
        print("file data exist")
    else:
        print("file data not exist,created")
        os.mkdir('data')
    if os.path.exists('data/bus'):
        print("file data/bus exist")
    else:
        os.mkdir('data/bus')
        print("file data/bus not exist,created")
    if os.path.exists('data/routes'):
        print("file data/routes exist")
    else:
        os.mkdir('data/routes')
        print("file data/routes not exist,created")
    buscsvKeys=["index/download",
        'fields.type', 
        'heading', 
        'id', 
        'lastStop',
        'lastUpdate',
        'lat',
        'lon',
        'name',
        'route'
        ]
    csvValuse=[None, None,None,None,None,None,None,None,None]


    if os.path.exists('data/bus/'+str(start_time)+'.csv'):
        print("file data/bus/"+str(start_time)+".csv exist")
    else:
        with open('data/bus/'+str(start_time)+'.csv', 'wb') as outcsv:
            writer = csv.DictWriter(outcsv, fieldnames = buscsvKeys)
            writer.writeheader()
        outcsv.close()
        print("file data/busRaw.csv not exist,created")
counter=0;
    
createFile()    
    
while True:
    resp = requests.get(url=url)
    try:
        data = resp.json()
    except:
        print ("This is an error message!")
        continue
    data = resp.json()
    data2=json_normalize(data)
    df = pd.DataFrame(data2, columns = [
        'fields.type', 
        'heading', 
        'id', 
        'lastStop',
        'lastUpdate',
        'lat',
        'lon',
        'name',
        'route'
    ]) 
    df.to_csv('data/bus/'+str(start_time)+'.csv', mode='a', header=False)
    time.sleep(3)
    print(df)

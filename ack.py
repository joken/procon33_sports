import chunk
from code import interact
import configparser
import requests
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from numpy import hamming
import numpy as np
import time
import json
import os


def GETtest():
    config = configparser.ConfigParser()
    config.read("config.ini")
    token = str(config["http_req"]["token"])
    domain = str(config["http_req"]["domain"])
    interval = float(config["http_req"]["interval_AutomaticGetting"])

    response = requests.get(domain + "/test?token="+token)
    print(response.status_code)

    # リクエストループ
    while(response.status_code != 200):
        print(">",end='',flush=True)
        response = requests.get(domain + "/test?token="+token)
        print(response.status_code)
        # dos判定の回避
        time.sleep(interval)
        if(response.status_code == 200):print("!",end="",flush=True)
        elif(response.status_code == 400):print(".",end="",flush=True)
        else:print("_",end='',flush=True)
    
    return response.json()

if __name__ == '__main__':
    print(GETtest())
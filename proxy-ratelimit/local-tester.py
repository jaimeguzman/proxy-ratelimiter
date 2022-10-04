from os import strerror
import time
import random
import threading
import requests
from requests.exceptions import HTTPError


endpoints = ("one", "two", "three", "four", "error","ping","/categories/ML1111","/categories/MLA97994" )

HOST = "http://127.0.0.1:8080/"

def run():
    while True:
        try:
            target = random.choice(endpoints)
            response = requests.get(HOST + target, timeout=10)
            print("HTTP_STATUS_CODE: "+" "+ str(response.status_code)+"\t connect to: "+str(HOST)+""+str(target) )

        except requests.RequestException:
            print("cannot connect "+str(HOST)+""+str(target) )
            time.sleep(1)


if __name__ == "__main__":
    for _ in range(4):
        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()

    while True:
        time.sleep(1)
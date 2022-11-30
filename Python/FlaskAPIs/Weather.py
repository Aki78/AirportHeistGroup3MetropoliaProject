import json
import requests
from flask import Flask, Response, request


layer = "clouds_new"
z = 200
x = 40
y = 30

request = "https: // tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid = {973b4a4b9535f80544f8201767f4c9b1}"

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

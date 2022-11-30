import json
import requests
from flask import Flask, Response, request
import mysql.connector

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

connection = mysql.connector.connect(
  host='127.0.0.1',
  port=3306,
  database='eu_flight_game',
  user='root',
  password='root'
)


@app.route('/top_ten')
def top_ten():
    try:
        args = request.args
        ex12_api_key = "873df6e3e029ba2d8538f1482461817f"
        location_name = str(args.get("city name"))
        request2 = "https://api.openweathermap.org/data/2.5/weather?q=" \
                   + location_name + "&appid=" + ex12_api_key + "&units=metric"
        response2 = requests.get(request2)
        if response2.status_code == 200:
            json_response2 = response2.json()
            return f"{json_response2['weather']['description']}{json_response2['main']['temp']}"

    except ValueError:
        response = {
            "message": "Invalid request",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


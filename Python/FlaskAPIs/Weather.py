from flask import Flask, Response, request
import requests
import json
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


@app.route('/get_weather')
def get_weather():
    try:
        args = request.args
        icao = str(args.get("icao"))
        sql = f"SELECT municipality FROM eu_airports WHERE ident = \"{icao}\";"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()

        ex12_api_key = "873df6e3e029ba2d8538f1482461817f"
        location_name = result[0][0]
        request2 = "https://api.openweathermap.org/data/2.5/weather?q=" + location_name + "&appid=" + ex12_api_key + "&units=metric"

        response2 = requests.get(request2)
        json_response2 = response2.json()
        return f"{location_name} {json_response2['weather'][0]['description']} {json_response2['main']['temp']}"

    except ValueError:
        response = {
            "message": "Invalid request",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)





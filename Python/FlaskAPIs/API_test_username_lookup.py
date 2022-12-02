from flask import Flask, Response, request
from flask_cors import CORS
import json
import mysql.connector

app = Flask(__name__)
cors = CORS(app)
app.config["JSON_SORT_KEYS"] = False
app.config['CORS_HEADERS'] = 'Content-Type'

connection = mysql.connector.connect(
  host='127.0.0.1',
  port=3306,
  database='eu_flight_game',
  user='root',
  password='root'
)


@app.route('/Account/<username>')
def login_credential_check(username):
    try:
        sql = f"select username from users where username = '{username}'"        
        
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        

        cursor.close()

        print(result[0][0])

        response = {
            "username": result[0][0]
        }

        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
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


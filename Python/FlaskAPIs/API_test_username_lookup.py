from flask import Flask, Response, request
from flask_cors import CORS
import json
import hashlib
import mysql.connector
import requests

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


@app.get('/Account/recaptcha')
def get_google_recaptcha():
    try:

        args = request.args
        key = args.get("skey")
        token = args.get("token")
        googleRequest = f"https://www.google.com/recaptcha/api/siteverify?secret={key}&response={token}"
        response = requests.get(googleRequest).json()  

        print("This", response)

        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

@app.post('/Account/createAccount')
def register_new_account_to_db():
    try:
        args = request.args
        username = args.get("username")
        password = args.get("password")
        salt = "5gz"

        db_password = password + salt
        hashed = hashlib.md5(db_password.encode())

        sql = f"insert into users(username, passwordhash, score) VALUES(\"{username}\",\"{hashed}\", 0);"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()

        response = {
            "message": "New user added"
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


@app.get('/Account/checkExist=<username>')
def check_existing_account(username):
    try:
        sql = f"select username from users where username = '{username}'"        
        
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()

        if cursor.rowcount > 0:
            response = {
                "message": "Exist"
            }
        else:
            response = {
                "message": "Nonexist"
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

@app.get('/Account/retrieve=<username>')
def login_credential_check(username):
    try:
        sql = f"select username from users where username = '{username}'"        
        
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        
        cursor.close()

        #print(result[0][0])

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


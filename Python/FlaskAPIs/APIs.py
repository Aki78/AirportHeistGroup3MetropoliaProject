from flask import Flask, Response, request
from flask_cors import CORS
import json
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

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def start(self):
        print("Starting Server")
        app.run(use_reloader=True, host=self.host, port=self.port)


@app.get('/Account/recaptcha')
def get_google_recaptcha():
    try:
        args = request.args
        key = args.get("skey")
        token = args.get("token")
        
        googleRequest = f"https://www.google.com/recaptcha/api/siteverify?secret={key}&response={token}"
        
        response = requests.get(googleRequest).json()  

        #print("This", response)

        return response

    except ValueError:
        response = {
            "message": "Invalid request",
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
        
        sql = f"insert into users(username, password, score) VALUES('{username}','{password}', 0);"
        
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
            "message": "Invalid request",
            "status": 400
        }
        
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        
        return http_response

@app.get('/Account/checkOldPass')
def check_old_password():
    try:
        args = request.args
        username = args.get("username")
        oldpass = args.get("oldpass")

        sql = f"select username, password from users where username = '{username}' and password = '{oldpass}';"
        
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
            "message": "Invalid request",
            "status": 400
        }
        
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        
        return http_response

@app.post('/Account/changePass')
def change_password():
    try:
        args = request.args
        username = args.get("username")
        newpass = args.get("newpass")

        sql = f"update users set password = '{newpass}' where username = '{username}';"
        
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()

        response = {
            "message": "Password changed"
        }
        
        return response

    except ValueError:
        response = {
            "message": "Invalid request",
            "status": 400
        }
        
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        
        return http_response

@app.post('/Account/deleteAccount')
def delete_account():
    try:
        args = request.args
        username = args.get("username")
        password = args.get("password")

        sql = f"delete from users where username = '{username}' and password = '{password}';"
        
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()

        response = {
            "message": "Account deleted"
        }
        
        return response

    except ValueError:
        response = {
            "message": "Invalid request",
            "status": 400
        }
        
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        
        return http_response

@app.get('/Account/checkExist=<username>')
def check_existing_account(username):
    try:
        sql = f"select username from users where username = '{username}';"        
        
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

@app.get('/Account/retrieve')
def login_credential_check():
    try:
        args = request.args
        username = args.get("userin")
        password = args.get("passin")
        
        sql = f"select username, password from users where username = '{username}' and password = '{password}';"        
        
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()

        if cursor.rowcount > 0:
            response = {
                "message": "Allow"
            }
        else:
            response = {
                "message": "Block"
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


@app.route('/top_ten')
def top_ten():
    try:
        sql = "SELECT username, score FROM users ORDER BY score DESC LIMIT 10;"
        
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()

        #print(result)

        json_response = json.dumps(result)
        http_response = Response(response=json_response, mimetype="application/json")
        
        return http_response

    except ValueError:
        response = {
            "message": "Invalid request",
            "status": 400
        }
        
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        
        return http_response

@app.route('/updatescore', methods=["PATCH"])
def patch_new_score():
    try:
        args = request.args
        username = args.get("username")
        new_score = args.get("score")

        sql1 = f"SELECT score FROM users WHERE username = '{username}';"
        sql2 = f"UPDATE users SET score = '{new_score}' WHERE username = '{username}';"
        
        cursor = connection.cursor()
        cursor.execute(sql1)
        result_score = cursor.fetchall()
        
        if int(new_score) > int(result_score[0][0]):
            cursor.execute(sql2)
            connection.commit()
            print(f"you beat your previous high score: {result_score[0][0]}")
            cursor.close()

            response = {
                "message": "New high score"
            }
        else:
            print(f"you did not beat your previous high score: {result_score[0][0]}")
            cursor.close()

            response = {
                "message": "Same score"

            }
        return response

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
    server = Server('127.0.0.1', '5000')
    server.start()

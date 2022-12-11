from flask import Flask, Response, request
from flask_cors import CORS
import json
import mysql.connector
import requests

connection = mysql.connector.connect(
    host='Aki78.mysql.pythonanywhere-services.com',
    port=3306,
    database='Aki78$airportheist',
    user='Aki78',
    password='HelloPython',
    autocommit=True
)

app = Flask(__name__, static_folder="./build", static_url_path="/")
app2 = Flask(__name__, static_folder="./templates/Publish", static_url_path="/")
app.config["JSON_SORT_KEYS"] = False
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def home():
    return "Hello World"

@app.route('/Home')
def index():
    return app.send_static_file('index.html')

@app.route('/game')
def game():
    return app2.send_static_file('index.html')

@app.route('/index.js')
def indexjs():
    return app2.send_static_file('index.js')

@app.route('/index.wasm')
def indexwasm():
    return app2.send_static_file('index.wasm')

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


@app.route('/index.pck')
def indexpck():
    return app2.send_static_file('index.pck')



@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


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
        
        sql = f"insert into users(username, password, score) VALUES(\"{username}\",\"{password}\", 0);"
        
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

#@app.route('/updatescore', methods=["PATCH"])
#def patch_new_score():
#    try:
#        args = request.args
#        username = args.get("username")
#        new_score = args.get("score")
#
#        sql1 = f"SELECT score FROM users WHERE username = '{username}';"
#        sql2 = f"UPDATE users SET score = '{new_score}' WHERE username = '{username}';"
#        
#        cursor = connection.cursor()
#        cursor.execute(sql1)
#        result_score = cursor.fetchall()
#        
#        if int(new_score) > int(result_score[0][0]):
#            cursor.execute(sql2)
#            connection.commit()
#            print(f"you beat your previous high score: {result_score[0][0]}")
#            cursor.close()
#
#            response = {
#                "message": "New high score"
#            }
#        else:
#            print(f"you did not beat your previous high score: {result_score[0][0]}")
#            cursor.close()
#
#            response = {
#                "message": "Same score"
#
#            }
#        return response
#
#    except ValueError:
#        response = {
#            "message": "Invalid request",
#            "status": 400
#        }
#        
#        json_response = json.dumps(response)
#        http_response = Response(response=json_response, status=400, mimetype="application/json")
#        
#        return http_response

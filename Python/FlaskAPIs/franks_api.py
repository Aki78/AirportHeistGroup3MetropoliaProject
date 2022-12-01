from flask import Flask, request, Response
import json
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',  # Change
    port=3306,  # Change
    database='eu_flight_game',
    user='root',  # Change
    password='root',  # Change
    autocommit=True
)

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route('/top_ten', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def top_ten():
    if request.method == 'GET':
        """for getting top ten players from our database"""
        try:
            sql = 'SELECT username, score FROM users ORDER BY score DESC LIMIT 10;'
            cursor = connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return json.dumps(result)
        except ValueError:
            response = {
                "message": "could not connect to get top 10 players",
                "status": 400
            }
            json_response = json.dumps(response)
            http_response = Response(response=json_response, status=400, mimetype="application/json")
            return http_response

    if request.method == 'POST':
        try:
            """for adding a new user to our database"""
            args = request.args
            username = str(args.get("username"))
            passwordhash = str(args.get("passwordhash"))
            sql = f"INSERT INTO users (username, passwordhash, score) VALUES (\"{username}\",\"{passwordhash}\", 0);"
            cursor = connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            connection.commit()
            return json.dumps(result)
        except ValueError:
            response = {
                "message": "could not connect to input new player",
                "status": 400
            }
            json_response = json.dumps(response)
            http_response = Response(response=json_response, status=400, mimetype="application/json")
            return http_response

    if request.method == 'PATCH':
        try:
            """for checking if new score is higher than previous and is yes adding to our database"""
            args = request.args
            username = str(args.get("username"))
            sql1 = f"SELECT score FROM users WHERE username = \"{username}\""
            cursor = connection.cursor()
            cursor.execute(sql1)
            result_score = cursor.fetchall()
            cursor.close()

            new_score = str(args.get("new_score"))
            if new_score > result_score:
                sql2 = f"UPDATE users SET score = \"{new_score}\" WHERE username = \"{username}\";"
                cursor = connection.cursor()
                cursor.execute(sql2)
                result = cursor.fetchall()
                cursor.close()
                connection.commit()
                return json.dumps(result)
        except ValueError:
            response = {
                "message": "could not connect to update score",
                "status": 400
            }
            json_response = json.dumps(response)
            http_response = Response(response=json_response, status=400, mimetype="application/json")
            return http_response

    if request.method == 'DELETE':
        try:
            """for removing a user from our database"""
            args = request.args
            username = str(args.get("username"))
            sql = f"DELETE FROM users WHERE username = \"{username}\";"
            cursor = connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return json.dumps(result)
        except ValueError:
            response = {
                "message": "could not connect to delete user information",
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
    """Test the functions. Print out expected values. If you have time, also use pytest"""
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

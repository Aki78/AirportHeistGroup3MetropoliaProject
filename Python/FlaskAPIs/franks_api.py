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
        try:
            sql = 'select * from top_players ORDER BY score desc LIMIT 10'
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
            args = request.args
            player_name = str(args.get("player_name"))
            password = str(args.get("password"))
            sql = f"INSERT INTO top_players (player_id, score) VALUES (\"{player_name}\",\"{password}\", 0);"
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
            args = request.args
            player_name = str(args.get("player_name"))
            sql1 = f"SELECT score FROM top_players WHERE player_id = \"{player_name}\""
            cursor = connection.cursor()
            cursor.execute(sql1)
            result_score = cursor.fetchall()
            cursor.close()

            new_score = str(args.get("new_score"))
            if new_score > result_score:
                sql2 = f"UPDATE top_players SET score = new_score WHERE player_id = \"{new_score}\";"
                cursor = connection.cursor()
                cursor.execute(sql2)
                result = cursor.fetchall()
                cursor.close()
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
            args = request.args
            player_name = str(args.get("player_name"))
            sql = f"DELETE FROM top_players WHERE player_id = \"{player_name}\";"
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


if __name__ == '__main__':
    """Test the functions. Print out expected values. If you have time, also use pytest"""
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

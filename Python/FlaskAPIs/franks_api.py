from flask import Flask, request, Response
import json
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',  # Change
    port=3306,  # Change
    database='flight_game',
    user='root',  # Change
    password='root',  # Change
    autocommit=True
)

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


def top_ten():
    sql = 'select * from top_players ORDER BY score desc LIMIT 10'
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return json.dumps(result)


@app.route('/topten', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def topten():
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
                "message": "could not connect and get top 10 players",
                "status": 400
            }
            json_response = json.dumps(response)
            http_response = Response(response=json_response, status=400, mimetype="application/json")
            return http_response

    if request.method == 'POST':
        try:
            args = request.args
            player_name = str(args.get("player_name"))
            sql = f"INSERT INTO top_players (player_id, score) VALUES (\"{player_name}\", 0);"
            cursor = connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            connection.commit()
            return json.dumps(result)
        except ValueError:
            response = {
                "message": "could not connect and input data",
                "status": 400
            }
            json_response = json.dumps(response)
            http_response = Response(response=json_response, status=400, mimetype="application/json")
            return http_response

    if request.method == 'DELETE':
        """Delete User and score"""
        """DELETE FROM top_players WHERE player_id = 'player-name';"""
        pass
    if request.method == 'PATCH':
        """get player's current highest score"""
        """SELECT score FROM top_players WHERE player_id = 'jenni2'"""
        """Change score"""
        """UPDATE top_players SET score = new_score WHERE player_id = 'player_name';"""
        pass


if __name__ == '__main__':
    """Test the functions. Print out expected values. If you have time, also use pytest"""
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

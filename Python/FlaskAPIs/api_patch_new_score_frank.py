from flask import Flask, Response, request
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


@app.patch('/updatescore/')
def patch_new_score():
    try:
        user = request.get_json()
        username = user['username']
        new_score = user['score']
        sql1 = f"SELECT score FROM users WHERE username = \"{username}\";"
        sql2 = f"UPDATE users SET score = \"{new_score}\" WHERE username = \"{username}\";"
        cursor = connection.cursor()
        cursor.execute(sql1)
        result_score = cursor.fetchall()
        if int(new_score) > int(result_score[0][0]):
            cursor.execute(sql2)
            connection.commit()
            print(f"you beat your previous high score: {result_score[0][0]}")
            cursor.close()
        else:
            print(f"you did not beat your previous high score: {result_score[0][0]}")
            cursor.close()
        return f"your score: {new_score}"

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


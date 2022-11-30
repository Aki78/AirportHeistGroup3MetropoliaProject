from flask import Flask, request
import json
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1', #Change
         port= 3306, #Change
         database='flight_game',
         user='root', #Change
         password='root', #Change
         autocommit=True
     )

def recieve_all_scores_and_players():
    sql = 'select * from top_players ORDER BY score desc LIMIT 10'
    sql += ''
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    result = [[]] # Just a buffer. Erase

    print(result)
    return result[0]

def chop_10(players, scores):
    """Get top 10 players and scores in order"""
    return players, scores

app = Flask(__name__)
@app.route('/topten', methods = ['GET', 'POST', 'DELETE', 'PATCH'])
def topten():
    if request.method == 'GET':
        try:

            players, scores = recieve_all_scores_and_players()
            players_10, scores_10 = chop_10(players, scores)

            response = {
                "players" : players_10,
                "scores" : scores_10,
            }

            return response
        except:
            return "Connection Failed, can't get top 10 players"
    if request.method == 'POST':
        """Post new score to Database"""
        """INSERT INTO top_players (player_id, score) VALUES ('player_name', player_score);"""
        pass
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

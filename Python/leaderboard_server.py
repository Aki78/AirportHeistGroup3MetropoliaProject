import tabulate
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='eu_flight_game',
    user='root',
    password='root',
    autocommit=True
)

def add_leaderboard_data(game_state):
    sql = (f"insert into top_players VALUES(\"{game_state['player']}\",{game_state['budget']});")

    cursor = connection.cursor()
    cursor.execute(sql)

player = "jenni2"
budget = 900
game_state = {
    "player": player,
    "budget": budget

}


def get_leaderboard_data():
    sql = ("select * from top_players order by score desc limit 10;")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("\nTop 10 players:")
    print(tabulate(result, tablefmt="double_outline"))


get_leaderboard_data()



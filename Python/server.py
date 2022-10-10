from flask import Flask, request
import json
import mysql.connector
import core
from time import sleep

#####################################
# Naming is from Godot's perspective#
#####################################

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)



app = Flask(__name__)
@app.route('/get_init')
def get_init():
    try:
        game_state = core.init_state()
        print("game init state is: ", game_state)

        return game_state
    except:
        # print(core.init_state())
        print("Init failed")
        return "No Init"

@app.route('/send_user_name', methods = ['POST'] )
def send_user_name():
    print("User name incoming Recieving")
    print(request.data)
    game_state = json.loads(request.data)
    print(game_state)
    print("name is: ", request.data)
    with open("game_state.json", "w") as outfile:
        outfile.write(json.dumps(game_state))

    return game_state

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

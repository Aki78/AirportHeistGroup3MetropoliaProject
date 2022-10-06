from flask import Flask, request
import json
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

def find_airport_and_location_by_icao(icao):
    sql = 'SELECT airport.name, country.name from airport join country using (iso_country)'
    sql += ' WHERE ident = "' + icao + '"'
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    print(result)
    return result[0][1], result[0][0]

app = Flask(__name__)
@app.route('/airport/<icao>')
def get_airport(icao):
    country  =""
    name = ""

    try:
        country, name = find_airport_and_location_by_icao(icao)

        response = {
            "icao" : icao,
            "airport_name" : name,
            "location" : country
        }

        return response
    except:
        return "Airport Not Found"


@app.route('/send', methods = ['POST'] )
def get_airport_rec():
    print("Recieving")
    print(request.data)

    return "A"


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'eu_flight_game',
    user = 'root',
    password = 'root',
    autocommit=True
)

#airportName = ["", ""]
airportPos = [[52.351389, 13.493889], [0, 0]]

sql = "select ident, name, latitude_deg, longitude_deg from eu_airports"

cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()

if cursor.rowcount > 0:
        for row in result:
            airportPos[1][0] = row[2]
            airportPos[1][1] = row[3]
            if distance.distance(airportPos[0], airportPos[1]).km < 1000 and airportPos[0] != airportPos[1]:
                print(row[1], "is reachable")
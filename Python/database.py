# data should be a dictionary with all the info
airports = {}
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='eu_flight_game',
    user='root',
    password='root',
    autocommit=True
)


# possibly make double these functions for plural
def get_airport_info():
    pass

# def get_weather():
#    pass

data_list = []

def datalist():
    sql = "select name, municipality, ident, latitude_deg, longitude_deg from eu_airports"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            data_list.append({"name": row[0], "municipality": row[1], "ident": row[2], "latitude_deg": row[3], "longitude_deg": row[4]})

    return


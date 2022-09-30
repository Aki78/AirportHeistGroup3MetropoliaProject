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

def pull():
    sql = "select name, municipality, ident, latitude_deg, longitude_deg from eu_airports"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[0]}, {row[1]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}")

    print(result)

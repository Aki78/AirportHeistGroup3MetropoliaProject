import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='eu_flight_game',
    user='root',
    password='root',
    autocommit=True
)

# def get_weather():
#    pass

# data should be a dictionary with all the info
airports = {}
coordinates_list = []
data_list = []

def get_airport_name():
    
    return

def get_coordinates():
    sql = "select latitude_deg, longitude_deg from eu_airports"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in result:
            coordinates_list.append((row[0], row[1]))
    
    return coordinates_list

def get_datalist():
    sql = "select name, municipality, ident, latitude_deg, longitude_deg from eu_airports"
    
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    
    if cursor.rowcount > 0:
        for row in result:
            data_list.append({"name": row[0], "municipality": row[1], "ident": row[2], "deg": (row[3], row[4])})
    
    print(data_list[0])
    
    return data_list

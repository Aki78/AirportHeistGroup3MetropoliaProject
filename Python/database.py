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

def get_new_coordinates(code):
    sql = "select latitude_deg, longitude_deg from eu_airports "
    sql += "where ident = '" + code + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    return (result[0][0], result[0][1])

def get_geo_airport_info(name):
    sql = "select name, municipality, country_name, ident, latitude_deg, longitude_deg from eu_airports "
    sql += "where name = '" + name + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    return result[0]

def get_airport_name(coordinates):
    sql = "select name, latitude_deg, longitude_deg from eu_airports"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in result:
            if (row[1], row[2]) == coordinates:
                return row[0]

def get_coordinates():
    coordinates_list = []

    sql = "select latitude_deg, longitude_deg from eu_airports"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in result:
            coordinates_list.append((row[0], row[1]))
    
    return coordinates_list

def get_datalist():
    data_list = []
    
    sql = "select name, municipality, ident, latitude_deg, longitude_deg, country_name from eu_airports"
    
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    
    if cursor.rowcount > 0:
        for row in result:
            data_list.append({"name": row[0], "municipality": row[1], "ident": row[2], "deg": (row[3], row[4]), "country": row[5]})
    
    #print(data_list[0])
    
    return data_list

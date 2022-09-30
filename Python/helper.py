def feet_to_meters(feet):
    meters = 0.3048 * feet
    return meters

def meters_to_km():
    pass

def get_distances():
    import mysql.connector

    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='root',
        autocommit=True
    )

    ICAO1 = input("Give an ICAO code: ")

    sql1 = "select latitude_deg, longitude_deg from airport where ident = '" + ICAO1 + "'"

    cursor = connection.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()

    from math import sin, cos, sqrt, atan2, radians

    # approximate radius of earth in km
    R = 6371.0

    lat_and_long = []
    if cursor.rowcount > 0:
        for row in result:
            print(f"The latitude for ICAO1 is {row[0]} and the location is {row[1]}")
            lat_and_long.append(row[0])
            lat_and_long.append(row[1])

    ICAO2 = input("Give another ICAO code: ")

    sql2 = "select latitude_deg, longitude_deg from airport where ident = '" + ICAO2 + "'"

    cursor = connection.cursor()
    cursor.execute(sql2)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in result:
            print(f"The latitude for ICAO1 is {row[0]} and the longitude is {row[1]}")
            lat_and_long.append(row[0])
            lat_and_long.append(row[1])

    lat_distance = (lat_and_long[2] - lat_and_long[0]) / 180 * 3.14
    long_distance = (lat_and_long[3] - lat_and_long[1]) / 180 * 3.14

    print(f" the difference in lat is {lat_distance} and the difference in long is {long_distance}.")

    a = (sin(lat_distance / 2)) ** 2 + cos(lat_and_long[0] / 180 * 3.14) * cos(lat_and_long[2] / 180 * 3.14) * (
        sin(long_distance / 2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    print(f" The distance between the two airports is {distance}km.")
    pass

def get_possible_flights():
    pass


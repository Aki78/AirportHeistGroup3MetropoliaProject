import mysql.connector
def get_employees_byLast_name():
    sql = "SELECT name from airport"
    # sql += " WHERE Last_name='" + last_name + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            # print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
            print(row)
    return
choose = input("would you like to A: add, F:find or Q:Quit ")

def add_airport(x):
    print(x)

def find_airport(x):
    print(x)

while 1:
    if choose == 'A':
        add_airport("A")
    elif choose == 'F':
        find_airport()
    else:
        break

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

print(get_employees_byLast_name())

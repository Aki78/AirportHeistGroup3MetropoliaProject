import mysql.connector
import hashlib
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='eu_flight_game',
         user='root',
         password='root',
         autocommit=True
)
email = input("Enter your email")
username = input("Enter your name:")
userpassword = input("Enter your password:")
password = userpassword
salt = "5gz"

dataBase_password = password + salt
hashed = hashlib.md5(dataBase_password.encode())

def login(email, username, password):
    sql = f"insert into users(email, username, passwordhash) VALUES(\"{email}\",\"{username}\",\"{hashed}\");"
    cursor = connection.cursor()
    cursor.execute(sql)
    return email, username, password

login(email, username, password)
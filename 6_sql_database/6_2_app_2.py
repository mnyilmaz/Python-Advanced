# BTK Academy
# Advanced Python Programming From Zero
# Lecture 5.1: SQL Database - SQL Database with Applications
# python 6_2_app_2.py
blank = "----------------------"

import mysql.connector

# Insert Function
def insert_Drivers(id, name, surname, team, point): # list
    
    sql = "INSERT INTO Drivers(id, name, surname, team, point) VALUES(%s, %s, %s, %s, %s)"
    values = (id, name, surname, team, point) # list
    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} record added into database.')
        print(f'Last added record ID: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print("Error", err)
    finally:
        connection.close()
        print("Database connection has closed")

##############################################################################################################

# Get Function including Where-Like-Order By
def get_Drivers():
    # cursor.execute('SELECT * FROM Drivers')
    # cursor.execute('SELECT Name,Surname FROM Drivers')
    # cursor.execute('SELECT Name,Surname FROM Drivers WHERE Team = "Ferrari"')
    # cursor.execute('SELECT Name,Surname FROM Drivers WHERE Team = "Ferrari" or Point = 219')
    # cursor.execute('SELECT Name,Surname FROM Drivers WHERE Team LIKE "%Ferari%"')
    # cursor.execute('SELECT Name,Surname FROM Drivers WHERE Team LIKE "%Ferari%" and Point = 219')
    # cursor.execute('SELECT Name,Surname FROM Drivers ORDER BY Point ASC') # default
    cursor.execute('SELECT Name,Surname FROM Drivers ORDER BY Point DESC')

    result = cursor.fetchall()
    # result = cursor.fetchone()
    
    for record in result:
        print(record)

##############################################################################################################

# Agreegate Functions: AVG, SUM, MAX, MIN...

def get_Info():

    # cursor.execute("SELECT COUNT(*) FROM Drivers")
    # cursor.execute("SELECT AVG(Point) FROM Drivers")
    # cursor.execute("SELECT SUM(Point) FROM Drivers")
    # cursor.execute("SELECT MAX(Point) FROM Drivers")
    # cursor.execute("SELECT MIN(Point) FROM Drivers")
    cursor.execute("SELECT MIN(Point) FROM Drivers")

    result = cursor.fetchone()
    for record in result:
        print(record)

##############################################################################################################

# Update Function

def get_Update():

    cursor.execute("UPDATE Drivers SET ID = 1 WHERE ID = 1")
    cursor.execute("UPDATE Drivers SET ID = 16 WHERE ID = 2")
    cursor.execute("UPDATE Drivers SET ID = 44 WHERE ID = 3")

    # cursor.execute("UPDATE Drivers SET Name = 'Max' WHERE ID = 1 ")
    # cursor.execute("UPDATE Drivers SET Surname = 'Verstappen' WHERE ID = 1 ")
    # cursor.execute("UPDATE Drivers SET Team = 'Red Bull' WHERE ID = 1 ")

##############################################################################################################

# Delete Function

def get_Delete():

    cursor.execute("DELETE FROM Drivers WHERE ID = 1")

##############################################################################################################

# Database connection
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "allard",
    database = "driversdb"
    )

# Database forming
cursor = connection.cursor()
# cursor.execute("CREATE DATABASE driversdb")
# cursor.execute("CREATE TABLE Drivers (id INT(25), name VARCHAR(255), surname VARCHAR(255), team VARCHAR(100), point INT(100))")
    
get_Update()
get_Delete()
get_Drivers()
get_Info()


id = int(input("ID: "))
name = input("Name: ")
surname = input("Surname: ")
team = input("Team: ")
point = int(input("Point: "))

insert_Drivers(id, name, surname, team, point)
    

# list = []

# while True:
    # id = int(input("ID: "))
    # name = input("Name: ")
    # surname = input("Surname: ")
    # team = input("Team: ")
    # point = int(input("Point: "))
    # list.append(id, name, surname, team, point)

#     result = input("Continue (Y/N): ")
#     if result == "N":
#         print("Datas recording into database...")
#         print(list)
#         insert_Drivers(list)

# insert_Drivers(list)

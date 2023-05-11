# BTK Academy
# Advanced Python Programming From Zero
# Lecture 5.1: SQL Database - SQL Database with Applications
# python 6_1_app_1.py
blank = "----------------------"

import mysql.connector


# Connection to the mysql database
# mydb = mysql.connector.connect(
#     host = "localhost", #192.1.1.1 server adress must display in here
#     user = "root",
#     password = "allard",
#     database = "newdb"
# ) 

# Forming new schema (database) from code inside mysql ide
# cursor = mydb.cursor()
# cursor.execute("CREATE DATABASE newdb") # sql querry

# Listing tables
# cursor.execute("SHOW DATABASES") # sql querry
# for x in cursor:
#     print(x)

# Forming a new table
# cursor.execute("CREATE TABLE drivers (name VARCHAR(255), surname VARCHAR(255))")

##############################################################################################################

# Application - Manager Database: Form a database that includes F1 Team Managers' informations
# Step 1: Connection with database

# Step 2: Form a db named "managerdb" and add the table named "Managers"
# crsr = mydb.cursor()
# crsr.execute("CREATE DATABASE managerdb")

# Step 3: Add columns named "ID", "Team Points", "Name", "Surname", "Birthdate", "Gender"
# crsr.execute("CREATE TABLE Managers (id INT(22), team_points INT(20), name VARCHAR(255), surname VARCHAR(255), team VARCHAR(100))")

##############################################################################################################

def insert_Manager(id, team_points, name, surname, team):
    connection = mysql.connector.connect(
        host = "localhost", 
        user = "root",
        password = "allard",
        database = "managerdb"
    ) 
    cursor = connection.cursor()
    #cursor.execute("CREATE DATABASE managerdb")
    #cursor.execute("CREATE TABLE Managers (id INT(22), team_points INT(20), name VARCHAR(255), surname VARCHAR(255), team VARCHAR(100))")

    sql = "INSERT INTO Managers(id, team_points, name, surname, team) VALUES(%s, %s, %s, %s, %s)"
    values = (id, team_points, name, surname, team)
    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} record added into database.')
        print(f'Last added record ID: {cursor.lastrowid}')

    except mysql.connector.Error as err:
        print("Error", err)
    finally:
        connection.close()
        print("Database connection is closed")

##############################################################################################################

def insert_Managers(list):
    connection = mysql.connector.connect(
        host = "localhost", 
        user = "root",
        password = "allard",
        database = "managerdb"
    ) 
    cursor = connection.cursor()
    #cursor.execute("CREATE DATABASE managerdb")
    #cursor.execute("CREATE TABLE Managers (id INT(22), team_points INT(20), name VARCHAR(255), surname VARCHAR(255), team VARCHAR(100))")

    sql = "INSERT INTO Managers(id, team_points, name, surname, team) VALUES(%s, %s, %s, %s, %s)"
    values = list
    cursor.executemany(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} record added into database.')
        print(f'Last added record ID: {cursor.lastrowid}')

    except mysql.connector.Error as err:
        print("Error", err)
    finally:
        connection.close()
        print("Database connection is closed")

list = []

while True:
    id = int(input("ID: "))
    tp = input("Team Points: ")
    name = input("Name: ")
    surname = input("Surname: ")
    team = input("Team: ")
    list.append((id, tp, name, surname, team))

    result = input("Continue (Y/N): ")
    if result == "N":
        print("Datas recording into database...")
        print(list)
        insert_Managers(list)

# insert_Manager(id, tp, name, surname, team)
# insert_Managers(list)

print()

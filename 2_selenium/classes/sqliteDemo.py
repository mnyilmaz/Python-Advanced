'''
Python - Selenium | SQLite


SQLite is a popular relational database management system 
(RDBMS) that is embedded into many applications and operating 
systems. It is a serverless, self-contained, and zero-configuration 
database engine that operates on a single file and provides a 
lightweight and efficient way to store, manage, and retrieve structured data.

1) Embedded Database: SQLite is designed to be embedded within applications, 
meaning it runs in-process with the application itself. There is no need for 
a separate server process or installation. The entire database is contained 
in a single file, making it easy to distribute and manage.

2) Relational Database Management System: SQLite follows the relational database 
model, where data is organized into tables consisting of rows and columns. It 
supports SQL (Structured Query Language) for managing and manipulating the data stored in the database.

3) Zero-Configuration: SQLite does not require any configuration or setup. 
It dynamically manages the database schema and performs automatic type 
conversion based on the data being stored. This simplicity makes it suitable 
for small to medium-sized applications and prototypes.

4) Cross-Platform: SQLite is cross-platform and works on various operating 
systems, including Windows, macOS, Linux, and mobile platforms such as Android 
and iOS. This allows applications to use SQLite consistently across different platforms.

5) Transaction Support: SQLite provides transaction support, allowing multiple 
database operations to be grouped together and treated as a single atomic unit. 
Transactions ensure data integrity and consistency by providing a way to roll back changes if an error occurs.

6) Extensibility: SQLite supports user-defined functions, custom collations, 
and virtual tables, allowing developers to extend its functionality and 
integrate it with their specific requirements.

7) Wide Language Support: SQLite has language bindings and APIs for multiple 
programming languages, including Python, C/C++, Java, Ruby, and more. This enables 
developers to interact with SQLite databases using their preferred programming language.

'''

import sqlite3

def list():
    connection = sqlite3.connect("database/example.db")
    cursor = connection.execute("select * from customers") # run "customer" querry in database
    
    for line in cursor:
        print(line[1]) # will print all customers' name in customers table
        
    connection.close()

if __name__ == "__main__":
    list()
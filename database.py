import mysql.connector as db

database = db.connect(
    host = "localhost",
    user = "root",
    password = "khoclocvighenMAH@",
    database = "testdata"
)

mycursor = database.cursor()
#deleta a table
#mycursor.execute("DROP TABLE accounts")

#create database
#mycursor.execute("CREATE DATABASE mydatabase") 

#Show databases
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

#create table
#mycursor.execute("CREATE TABLE account (user VARCHAR(255), password VARCHAR(255))")

#create table primary key
# mycursor.execute("CREATE TABLE accounts (user VARCHAR(255) PRIMARY KEY, password VARCHAR(255))")

#show table
# mycursor.execute("SHOW TABLES")
# for i in mycursor:
#     print(i)


#insert to tables
sql = "INSERT INTO accounts (user, password) VALUES (%s, %s)"
val = ('bossbaby2120052', '123456')
mycursor.execute(sql, val)
database.commit()
print(mycursor.rowcount, "record inserted.")
if (mycursor.rowcount != 0):
    print("Account has created")
else:
    print("Account hasn't created")
print("1 record inserted, ID:", mycursor.lastrowid)
print("")
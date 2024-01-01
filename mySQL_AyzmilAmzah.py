import mysql.connector

mydb=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='Bibi100%',
    db = 'mydb'
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE myDB") # #use this to create db

# mycursor.execute('SHOW DATABASES') 
# for i in mycursor:
#     print(i) ##another way to check db existence

# mycursor.execute("CREATE TABLE cutomers (name VARCHAR(255), address VARCHAR(255))" ) 
# use the above line to create a table

# mycursor.execute('SHOW TABLES')
# for x in mycursor:
#     print(x)

# # figure 1 : the code to create a table with primary key
# mycursor.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))')

# # figure 2 : to alter existed table  to create primary key
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 

# # To fill up the table
# # use Insert Into
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute (sql, val)

# mydb.commit()

# print(mycursor.rowcount,'record inserted')

# # INSERT INTO MULTIPLE ROWS
# # USE executemany.method()
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#     ('Peter', 'Lowstreet 4'), 
#     ('Amy','Apple st 652'),
#     ( 'Hannah', 'Mountain 21'),
#     ('Michael', 'Valley 345'), 
#     ('Sandy', 'Ocean blvd 2'), 
#     ('Betty', 'Green Grass 1'),
#     ('Richard', 'Sky st 331'),
#     ('Susan', 'One way 98'), 
#     ('Vicky', 'Yellow Garden 2'), 
#     ('Ben', 'Park Lane 38'),
#     ('William', 'Central st 954'),
#     ('Chuck', 'Main Road 989'),
#     ('Viola', 'Sideway 1633')]

# mycursor.executemany (sql, val)

# mydb.commit ()

# print(mycursor. rowcount, "was inserted.")

# # GET INSERTED ID
# sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
# val = ('Michelle', 'Blue Village')

# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)

# # 'SELECT * FROM any_table' = SELECT ALL 
# mycursor.execute('SELECT * FROM customers')

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)


# # 'SELECT column FROM any_table'
# mycursor.execute('SELECT name, address FROM customers')

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# use fetchone() method to find the first row
# mycursor.execute('SELECT * FROM customers')

# myresult = mycursor.fetchone()

# print(myresult)

# # SELECT with a filter
# sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# # SELECT RECORDS THAT STARTS, INCLUDES OR END WITH GIVEN LETTER OR PHRASE "%%"
# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

# mycursor.execute(sql)

# myresult=mycursor.fetchall()

# for x in myresult:
#     print(x)
    
# sql = "SELECT * FROM customers WHERE address  = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# SORT THE RESULT
# ORDER BY
# sql = "SELECT * FROM customers ORDER BY name"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# sql = "SELECT * FROM customers ORDER BY name DESC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# TO DELETE ANY RECORD WHERE ADDRESS IS "MOUNTAIN 21"
# sql ="DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# sql ="DELETE FROM customers WHERE address = %s"
# adr =("Yellow Garden 2",)
# mycursor.execute(sql, adr)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# # DROP TABLE / DROP TABLE IF EXISTS
# # DROP TABLE -> To delete and existing table
# sql="DROP TABLE customers"
# mycursor.execute(sql)

# DROP TABLE IF EXISTS
# sql = "DROP TABLE IF EXISTS users"
# mycursor.execute(sql)

# # UPDATE THE TABLE
# sql="UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

# sql="UPDATE customers SET address =%s WHERE address = %s"
# val=("Valley 345", "Canyon 123")
# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

# # LIMIT THE OUTPUT
# mycursor.execute("SELECT * FROM customers LIMIT 5")
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)

# # LIMIT THE OUTPUT BUT START FROM ANOTHER POSITION
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)

# mycursor.execute("CREATE TABLE users(name VARCHAR(255), fav VARCHAR(255))")
# mycursor.execute("CREATE TABLE products(id INT, name VARCHAR(255))")

# sql=("INSERT INTO users (name, fav) VALUES (%s, %s)")
# val=[
#     ('John','154'),
#     ('Peter','154'),
#     ('Amy','155'),
#     ('Hannah',''),
#     ('Michael',''),
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount , "was inserted.")

# sql=("INSERT INTO products (id, name) VALUES (%s, %s)")
# val=[
#     ('154','Chocolate Heaven'),
#     ('155','Tasty Lemons'),
#     ('156','Vanilla Dreams'),
    
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount , "was inserted.")

# # JOIN & INNER JOIN
# sql="SELECT \
#     users.name AS user, \
#     products.name AS favourite \
#     FROM users \
#     INNER JOIN products ON users.fav = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# # LEFT JOIN
# sql="SELECT \
#     users.name AS user, \
#     products.name AS favourite \
#     FROM users \
#     LEFT JOIN products ON users.fav = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# RIGHT JOIN
# sql="SELECT \
#     users.name AS user, \
#     products.name AS favourite \
#     FROM users \
#     JOIN products ON users.fav = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
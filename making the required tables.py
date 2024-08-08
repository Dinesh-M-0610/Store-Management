import mysql.connector
mydb1 = mysql.connector.connect(host="localhost",user="root",passwd="1234")
mycursor1 = mydb1.cursor()
mycursor1.execute("create database annachi_stores")
mydb1.commit()
print("Created Database annachi_stores successfully")
mydb1.close()
mydb2 = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="annachi_stores")
mycursor = mydb2.cursor()
mycursor.execute("create table items_in_store(item_no integer,item_namechar(20),price integer)")
mycursor.execute("create table total_sales(date char(20),total_amount integer)")
mycursor.execute("create table staff’s(Idno integer,Name char(20),genderchar(2),shift char(2),Salary integer)")
print("Created the required tables successfully")
sql1 = "insert into items_in_store values(%s,%s,%s)"
sql2 = "insert into total_sales values(%s,%s)"
sql3 = "insert into staff’s values(%s,%s,%s,%s,%s)"
val1 = [(1,'soap',30),(2,'chocolate',10),(3,'shampoo',50),(4,'pencil',5),(5,'pen',50),(6,'chart',5)]
val2 = [("2022-10-4",6590),("2022-10-6",6590),("2022-11-19",2901),("2022-11-20",1051)]
val3 = [(1231,"shivram",'m','m',15000),(1232,"prajan",'m','e',15000),(1233,"remo",'m','e',35000),(1234,"shree devi",'f','m',20000),(1235,"ponpriya",'f','e',25000),(1236,"shaffi",'m','m',25000),(1237,'vishal','m','e',25000),(1238,"dinesh",'m','m',35000),(1239,"akash",'m','e',35000)]
for i1 in val1:
    mycursor.execute(sql1,i1)
mydb2.commit()
print("Added Datas in items_in_store table")
for i2 in val2:
    mycursor.execute(sql2,i2)
mydb2.commit()
print("Added Datas in total_sales table")
for i3 in val3:
    mycursor.execute(sql3,i3)
mydb2.commit()
print("Added Datas in staff’s table")
mydb2.commit()
print("CREATED ALL THE REQUIRED THINGS IN THIS SYSTEM")

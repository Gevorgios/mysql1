import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="####",
    user="####",
    password="####",
    database="fruits_and_vegetables"
)

MyCur = mydb.cursor()
sql = """SELECT * FROM fruits_and_vegetables"""
MyCur.execute(sql)

result = MyCur.fetchall()
for element in result:
    print(element)

sql = """SELECT * FROM fruits_and_vegetables WHERE type = "Овощ" """
MyCur.execute(sql)

result = MyCur.fetchall()
for element in result:
    print(element)


sql = """SELECT * FROM fruits_and_vegetables WHERE type = "Фрукт" """
MyCur.execute(sql)

result = MyCur.fetchall()
for element in result:
    print(element)

sql = """SELECT name FROM fruits_and_vegetables"""
MyCur.execute(sql)

result = MyCur.fetchall()
for element in result:
    print(element)

sql = """SELECT DISTINCT color FROM fruits_and_vegetables"""
MyCur.execute(sql)

result = MyCur.fetchall()
for element in result:
    print(element)

sql = """SELECT * FROM fruits_and_vegetables WHERE type = "Фрукт" AND color = "Красный" """
MyCur.execute(sql)

result = MyCur.fetchall()
for element in result:
    print(element)


sql = """SELECT * FROM fruits_and_vegetables WHERE type = "Овощ" AND color = "Оранжевый" """
MyCur.execute(sql)

result = MyCur.fetchall()
for element in result:
    print(element)

MyCur.close()
mydb.commit()
mydb.close()
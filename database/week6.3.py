#CT60A4304_01.06.2020 Basics of Database Systems
#week6.3, python and SQL
#Aatu Laitinen


import sqlite3

yhteys = sqlite3.connect('week6.db')
print("connection success.")

yhteys.execute("DELETE FROM employees WHERE ID=1;")

print("data deleted successfully")

data = yhteys.execute("SELECT * FROM employees")

rows = data.fetchall()

print("Number of rows in database =",len(rows))

yhteys.execute("DROP TABLE employees")

print("\nTable removed successfully")

yhteys.close()


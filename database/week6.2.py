#CT60A4304_01.06.2020 Basics of Database Systems
#week6.2, python and SQL
#Aatu Laitinen


import sqlite3

yhteys = sqlite3.connect('week6.db')
print("connection success.")

yhteys.execute("UPDATE employees SET name = 'Mary',\
                address = '1st alley',\
                phone = 30042399 WHERE id = 1")

yhteys.execute("UPDATE employees SET name = 'Gary',\
                address = '3rd avenue',\
                phone = 30123542 WHERE id = 2")

print("Data updated successfully")

data = yhteys.execute("SELECT * FROM employees")

for info in data:
    print("employee",info[0])
    print("id =",info[0])
    print("name =",info[1])
    print("address =",info[2])
    print("phone =",info[3],"\n")

yhteys.close()


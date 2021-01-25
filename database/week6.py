#CT60A4304_01.06.2020 Basics of Database Systems
#week6, python and SQL
#Aatu Laitinen


import sqlite3

yhteys = sqlite3.connect('week6.db')
print("connection success.")


    
yhteys.execute('''CREATE TABLE employees
                (id INT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                phone INT NOT NULL);''')

print("Table emplyees created successfully")

yhteys.execute("INSERT INTO employees \
                VALUES(1,'John','5th avenue','300423942'),\
               (2,'Julie','3rd road','309432424'),\
               (3,'Max','8th boulevard','32135464'),\
               (4,'Chris','2nd street','38532453')")
yhteys.commit()
print("Values inserted successfully\n")

data = yhteys.execute("SELECT * FROM employees")

for info in data:
    print("employeee",info[0])
    print("id =",info[0])
    print("name =",info[1])
    print("address =",info[2])
    print("phone =",info[3],"\n")

yhteys.close()
    


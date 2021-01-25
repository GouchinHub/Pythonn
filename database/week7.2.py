#CT60A4304_01.06.2020 Basics of Database Systems
#week6, python and SQL
#Aatu Laitinen


import sqlite3
import time

yhteys = sqlite3.connect('week7.db')
print("connection success.")

yhteys.execute("DROP TABLE employees")
    
yhteys.execute('''CREATE TABLE employees (
                [EmployeeId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                [LastName] NVARCHAR(20)  NOT NULL,
                [FirstName] NVARCHAR(20)  NOT NULL,
                [Title] NVARCHAR(30),
                [ReportsTo] INTEGER,
                [BirthDate] DATETIME,
                [HireDate] DATETIME,
                [Address] NVARCHAR(70),
                [City] NVARCHAR(40),
                [State] NVARCHAR(40),
                [Country] NVARCHAR(40),
                [PostalCode] NVARCHAR(10),
                [Phone] NVARCHAR(24),
                [Fax] NVARCHAR(24),
                [Email] NVARCHAR(60),
                FOREIGN KEY ([ReportsTo]) REFERENCES "employees" ([EmployeeId]) 
                    ON DELETE NO ACTION ON UPDATE NO ACTION)''')

print("Table emplyees created successfully")

for i in range(200):
    fname = "fname"+str(i)
    lname = "lname"+str(i)
    title = "title"+str(i)
    address = "street"+str(i)
    yhteys.execute("INSERT INTO employees ([EmployeeId],[FirstName],[LastName],[Title],[Address])\
                    VALUES(?,?,?,?,?)",(i,fname,lname,title,address))

data = yhteys.execute("SELECT[FirstName],[LastName] FROM employees")


tic = time.perf_counter()
for info in data:
    print("first name =",info[0])
    print("last name =",info[1])
toc = time.perf_counter()
print("time take :",toc - tic)


yhteys.execute("CREATE UNIQUE INDEX employee_name \
                ON employees ([FirstName],[LastName])")


yhteys.close()
    


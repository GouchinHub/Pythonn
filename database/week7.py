#CT60A4304_01.06.2020 Basics of Database Systems
#week7, python and SQL
#Aatu Laitinen


import sqlite3

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

yhteys.execute("CREATE UNIQUE INDEX employee_name \
                ON employees ([FirstName],[LastName])")

yhteys.execute("INSERT INTO employees ([EmployeeId],[FirstName],[LastName],[Title])\
                VALUES(1,'John','wick','CEO'),(2,'Will','Smith','Janitor'),\
                (3,'Bob','Ross','Secretary')")

data = yhteys.execute("SELECT [EmployeeId],[FirstName],[LastName],[Title] FROM employees")

for info in data:
    print("employee id",info[0])
    print("first name =",info[1])
    print("last name =",info[2])
    print("Title =",info[3],"\n")

yhteys.close()
    


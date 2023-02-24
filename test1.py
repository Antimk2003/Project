
import pymysql

# Connect to MySQL
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="Antimk",
  database="test"
)

# Create a cursor object
mycursor = mydb.cursor()
code = int(input("Enter code :"))
name = input("enter name: ")
salary = int(input("enter salary:"))
query = """insert into empy values({},'{}',{})""".format(code,name,salary)
mycursor.execute(query) 

# Commit changes
mydb.commit()
print("data inserted successfully...")

# Close the connection
mydb.close()

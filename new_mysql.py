
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
while True:
    code = int(input("Enter code :"))
    name = input("enter name: ")
    salary = int(input("enter salary:"))
    query = """insert into empy values({},'{}',{})""".format(code,name,salary) 
    mycursor.execute(query) 
    show = mycursor.fetchall()
    print(show)

# Commit changes
    mydb.commit()
    print("data inserted successfully...")
    x = int(input("1->Enter more/n2->Exit/nEnter choice: "))
    if x==2:
        break 
# Close the connection
    mydb.close()

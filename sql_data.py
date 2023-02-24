import pymysql

# Connect to MySQL
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="Antimk",
  database="piyush"
)

cur = mydb.cursor() 
# Create a cursor object
mycursor = mydb.cursor()
qry = "Create table school(stu_name varchar(20),stu_addres varchar(10),stu_code int(10),stu_subject varchar(15))" 
qrey = """insert into school values("barkha","m.p",103,"mca"),("gulpit","ujjain",106,"b.tach"),("purvi","aasta",107,"M.A")"""
qry2 = "select distinct stu_code from school"
qry1 = "select sum(stu_code) from school"
qry3 = "select max(stu_code) from school"
qry4 = "select min(stu_code) from school"
mycursor.execute(qry4) 

show =mycursor.fetchone()
print(show)
# Commit changes
mydb.commit()
print("data inserted successfully...")

# Close the connection
mydb.close()
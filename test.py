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
qry = "Create table teachar(name varchar(10),branch varchar(10),id_no int)"
value = """insert into teachar values("antima","teachar",75875),("sumanshu","professor",747110),("deepak","gest",812066)"""
add ="alter table teachar add phone_no int(20)"
update = "update teachar set phone_no = 3370 where id_no =812066"
add1 ="alter table teachar add surname varchar(20)"
delete ="alter table teachar drop surname" 
select ="select max(id_no) from teachar"
lest ="select min(id_no)from teachar"

mycursor.execute(lest) 

show =mycursor.fetchone()
print(show)
# Commit changes
mydb.commit()
print("data inserted successfully...")

# Close the connection
mydb.close()

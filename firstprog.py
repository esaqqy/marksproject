import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="databas1"
)
sql_Query = "SELECT * FROM mark"
mycursor = mydb.cursor()
mycursor.execute(sql_Query)
policydetails = mycursor.fetchall()
print(policydetails)

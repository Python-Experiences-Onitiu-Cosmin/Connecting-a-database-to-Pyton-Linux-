import MySQLdb

db = MySQLdb.connect('localhost', 'root', 'cisco', 'python')

if db == None:
     print "Error connect to the database"
else:
     print "All Good!"

cursor = db.cursor()
cursor.execute("SELECT VERSION();")
data = cursor.fetchall()

try:
   cursor.execute("DROP TABLE IF EXISTS HOP")
   cursor.execute("""CREATE TABLE HOP(
                         NUME CHAR(20) NOT NULL,
                         VARSTA INT,
                         SEX CHAR(1),
                         INTEREST CHAR(20)); 
                  """)
   db.commit()
   print "TABLE CREATED"
except EXCEPTION:
     print "Operation Failed"
     db.rolledback()

sql ="""INSERT INTO HOP (NUME, VARSTA, GENDER, ITNEREST) VALUES("Ramon",23,"M","Python")"""
try:
    cursor.execute(sql)
    db.commit()
except Exception
    print "Can't add to database 2"
    db.rollback()

sql_query = (("Ramon2",24,"M","Programare"),("Ramon3",25,"F","Programare"))
for user in sql_query:
    try:
        cursor.execute('INSERT INTO HOP (NUME,VARSTA,GENDER,INTEREST),VALUES("%s","%d","%s","%s")' % (user[0],user[1],user[2],user[3]))
    except Exception:
        print "Operation not working"
        db.rollback()

db.close()
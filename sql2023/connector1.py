from mysql import connector
myDbConnection=connector.connect(host='localhost',user='root',password='root',database='python2023')
print(myDbConnection)
c1=myDbConnection.cursor()
c1.execute("insert into emp values()")
c1.execute("insert into emp values(200,'def',2000,20)")
myDbConnection.commit()
myDbConnection.close()

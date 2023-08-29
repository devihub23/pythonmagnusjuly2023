from mysql import connector
myDbConnection=connector.connect(host='localhost',user='root',password='root',database='python2023')
print(myDbConnection)
c1=myDbConnection.cursor()
c1.execute("drop table if exists emp")
c1.execute("create table emp(empno int,ename varchar(20),sal int,deptno int)")
c1.close()

from mysql import connector
dbconnection = connector.connect(host='localhost',user='root',password='root',database='Python2023')
print(dbconnection)
c = dbconnection.cursor()


class Table:
    def create(self):
        c.execute("create table list(no int,name varchar(20),dept varchar(20),count int)")
        dbconnection.commit()
        dbconnection.close()

    def insert(self):
        itemno=int(input("enter no: "))
        itemname=input("enter name: ")
        itemdept=input("enter dept: ")
        itemcount=int(input("enter count: "))
        c.execute("insert into list(no, name, dept, count) values(%s, %s, %s, %s)", (itemno, itemname, itemdept, itemcount))
        dbconnection.commit()
        dbconnection.close()

    def update(self):
        c.execute("update list set name='silver', count=100 where no=4")
        dbconnection.commit()
        dbconnection.close()

    def delete(self):
        c.execute("delete from list where no=2")
        dbconnection.commit()
        dbconnection.close()

    def alter(self):
        c.execute("alter table list add cost float")
        c.execute("alter table list change no id int")
        dbconnection.close()

    def select(self):
        sql = "select * from list where count=5"
        c.execute(sql)
        result = c.fetchone()
        for i in result:
            print(i)
        dbconnection.close()


obj1 = Table()
#obj1.create()
#obj1.insert()
#obj1.update()
#obj1.delete()
#obj1.alter()
obj1.select()

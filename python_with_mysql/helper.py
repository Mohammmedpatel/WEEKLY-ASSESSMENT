import mysql.connector as connector
class Md:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                      port='3306',
                      user='root',
                      password='Patelmd@42400',
                      database='pythontest')
        query="create table if not exists user(userid int primary key,username varchar(50),phone varchar(10))"
        cur=self.con.cursor()
        cur.execute(query)
        # print("created")

    def insert_user(self,userid,username,phone):
        query="insert into user(userid,username,phone) values({},'{}','{}')".format(userid,username,phone)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("user inserted")

    def fetch_all(self):
        query="select * from user"
        c=self.con.cursor()
        c.execute(query)
        for row in c:
            print("user id: ",row[0])
            print("user name: ",row[1])
            print("phone: ",row[2])
            print()
            print()

    def delete_user(self,userid):
        query="delete from user where userid={}".format(userid)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        # print("deleted")

    def update_user(self,userid,newname,newphone):
        query="update user set username='{}',phone='{}' where userid={}".format(newname,newphone,userid)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        # print("updated")

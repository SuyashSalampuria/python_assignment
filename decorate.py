# !/usr/bin/python
class MyException(Exception):
    pass
import MySQLdb
db = MySQLdb.connect(host='localhost', user='suyash' , passwd='asus12',db='users')
def hello_decorator(func): 
    def check():
        d=func()
        cur=db.cursor()
        cur.execute("select * from user")
        for row in cur.fetchall() :
            if(d==row[0]):
                return True 
        raise MyException('User not found')
        return False       
    return check

from decorate import hello_decorator
import MySQLdb
from scrap import scrap
db = MySQLdb.connect(host='localhost', user='suyash' , passwd='asus12',db='users')
nams=None
citys=None
works=[]
favs={}
foun=False

@hello_decorator
def usee():
    return username
username = input("Enter username")
username=str(username)
usee()
status=usee()
if(status):
    scrap(username,nams,citys,works,favs,foun)
else:
    raise Exception("Not found")

from decorate import hello_decorator
from Person import Person
from Person import MyException
from scrap import scrap
import unittest
nams=None
citys=None
works=[]
favs=[]
foun=False
person=Person('Ayush Jain', city='Roorkee',work=["hbjsd"])
@hello_decorator
def usee():
    return 'ayushjainaj20'
class SimpleTest(unittest.TestCase): 
    global t 
    def test(self):         
        self.assertTrue(usee(),True) 
   
    t=scrap('ayushjainaj20',nams,citys,works,favs,foun)
    def test_name(self):
        self.assertTrue(t[0],'Ayush Jain')
    def test_city(self):
        self.assertTrue(t[1],'Roorkee')
    def test_work(self):
        self.assertTrue(t[2],['Cinematic Section,IIT Roorkee', 'IMG, IIT Roorkee'])
    def test_fav(self):
        self.assertTrue(t[3],{'Other': ['Dhruv Sleeping in Unusual Places', 'Gaurav V/S Mankind', 'Cheerful Nihilism', 'ｈｉｔｅｓｘｈ ヤング・ウチハ', 'Emotional Introvert', "Students' Affairs Council, IIT Roorkee", 'Choreography and Dance section IIT Roorkee', 'Data Science Group, IITR', 'Enactus IIT Roorkee', 'IMG, IIT Roorkee', 'Sarcasm', 'Iron Man - The Hustler', 'Kya-Gift-Du', 'Feynman Fans', 'ISRO - Indian Space Research Organisation', 'National Geographic TV', 'and more']})

    def test_person(self):
        self.assertTrue(person.name,'Ayush Jain')
    def test_person2(self):
        self.assertTrue(person.city,'Roorkee')
    def test_person3(self):
        with self.assertRaises(MyException):
            Person('Ayush Jain', city='Roorkee',works='vwed')
   
if __name__ == '__main__': 
    unittest.main() 
    
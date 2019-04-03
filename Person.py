# !/usr/bin/python
class MyException(Exception):
    pass
class Person() : 
    def __init__(self, name, city="Roorkee" , **kwargs): 
        self.name = name
        self.city = city
        for key, value in kwargs.items():
            if(key=='work'):
                if(len(value)>0):
                    self.work = value
            else:
                raise MyException('No work found')

    def show(self):
        print(f"My name is {self.name} and my current city is {self.city}")
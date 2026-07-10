class student:
    def __init__(self):
        self.name = "Bhabina"
        self.num = 101

    def study(self):
        print("Bhabina is studying")


s1 = student()
print(s1.num)
s1.study()


class student2:
    def details(self):
        print("Had breakfast")


s2 = student2()
s2.details()
student2.details(s2)


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = student("Bhabina", 20)
s2 = student("Disha", 20)
s3 = student("Arbiya", 20)
print(s1.name,s2.name, s3.name)
print(s1.age,s2.age,s3.age)


class bank:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print(self.balance)


account = bank(5000)
account.check_balance()


class user:
    def __init__(self, name):
        self.name = name

    def login(self):
        print(self.name, "logged in")


u1 = user("nibba")
u2 = user("nibbi")
u1.login()
u2.login()

#inheritance
class Animal:
    def wild(self):
        print(" wild Animal")


class dog(Animal):
    def domestic(self):
        print("Dog is a domestic Animal")


s = dog()
s.wild()
s.domestic()


# inheritance
class thatha:
    def land(self):
        print("thatha's land")


class appa(thatha):
    def house(self):
        print("appa's land")


class maga(appa):
    def bike(self):
        print("son has a bike")


obj = maga()
obj.land()
obj.house()
obj.bike()


# multiplelevel inheritance
class father:
    def house(self):
        print("father's house")


class mother:
    def land(self):
        print("mother's land")


class son(father, mother):
    def property(self):
        print("Son gets both father's and mother's property ")


s1 = son()
s1.house()
s1.land()
s1.property()


#hierarchical inheritance


class father:
    def property(self):
        print("Father's property")


class daughter(father):
    def land(self):
        print("50%  property to daughter")


class son(father):
    def house(self):
        print("50%  property to son")


s1 = son()
s1.house()
s1.property()

s2 = daughter()
s2.land()
s2.property()


class student:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

s = student("Queen")
print(s)

#decorators
def login(func):
    def wrapper():
        print("checking login")
        func()
    return wrapper
@login
def dashboard():
    print("Dashboard page")
dashboard()


def message(func):
    def wrapper():
        print("function started")
        func()
        print("function ended")
    return wrapper

@message
def hello():
    print("hello python")
hello()


def Hiii():
    print("Full stack")
Hiii()


def Hey():
    print("Development")
Hey()

import json
student = {
    "name": "Bhabina",
    "age": 22,
}
data = json.dumps(student)
print(data)


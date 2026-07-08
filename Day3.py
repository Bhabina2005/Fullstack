#Tuples

students = ("Alice", "Bob", "Charlie")
print(students)
numbers = (1, 2, 3, 4, 5)
print(numbers)

students=["Alice", "Bob", "Charlie"]
print(students[-2])

numbers=[1, 2, 3, 4, 5]
print(numbers[-3])

data=(1,2,3)
data[0] = 200
print(data)

x = (1, 2, 3, 4, 1, 1, 1, 6, 7, 8)
print(x.count(4))
print(x.count(1))

x = ("A", "B", "C", "A", "B")
print(x.count("A"))
print(x.index("A"))

#Slice
num = (10, 20, 30, 40, 50, 70)
print(num[1:4])
print(num[3:4])

#sets
x={1,2,3,4,5,2,3,7}
print(x)
data = {1, 2, 3,4,5,6,7}
data.add(4)
data.remove(1)
print(data)

#union
x={1,2,3,4,5}
y={4,5}
print(x|y)

#interscetion
a = {1, 2, 4, 5, 2}
b = {4, 5, 2}
print(a & b)

#Functions - Reusable block of code used to perform specific task

def greeting():
    print("hello students")
greeting()

#functions with  return

def add():
    return 10+20
result = add()
print(result)


def sub():
    return 10-20
result = sub()
print(result)


def mul():
    return 10*20
result = mul()
print(result)


def div():
    return 10/20
result = div()
print(result)


def add(a,b):
    print(a+b)
add(10,20)

#arguments

def add(*num):
        total = 0
        for i in num:
             total+=i
        print(total)
add(10,20,30,40,50,60)

def student_info(**details):
    print(details)

student_info(
    name = "Disha",
    age = 20,
    job = "sde"
)

def student(**details):
    print("name : ", details["name"])
    print("age :" , details["age"])
    print("job:", details["job"])

student(
    name="Bhabina",
    age = 20,
    job="sde",
)


#square root

def square(n):
    return n * n
print(square(9))

#using lambda function

square = lambda x: x*x
print(square(25))

add = lambda a,b:a+b
print(add(10,20))


#To find even and odd

n = int(input("enter a number :"))
if n % 2 == 0:
    print("even")
else:
    print("odd")


#using lamda function

num = lambda x: "Even" if x % 2 == 0 else "odd"
print(num(2))
print(num(3))


alpha = lambda x : x.upper()
print(alpha("abc"))

#to find length
alpha = lambda text: len(text)
print(alpha("Disha"))

file = open("student.txt", "a")
file.write("\nHello Disha")
file.close()
print("Data written successfully")

file = open("student.txt", "r")
data = file.read()
print(data)
file.close()

file = open("student.txt", "a")
file.write("\nHIIIII")
file.close()

print("Data appended successfully")

file = open("student.txt", "r")
print(file.read())
file.close()

a = 10
b = 0
print(a/b)
try:
    a = 10
    b = 0
    print(a/b)
except:
    print("Something went wrong")

try:
    num=int(input("enter the number "))
except:
    print("only number allowwed")

try:
    a = int(input("enter A: "))
    b = int(input("enter B "))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("enter only numbers")

try:
    file = open("data.txt")
    print(file.read())
except:
    print("file error")
finally:
    print("program completed")

try:
    print(10/2)
except:
    print("error")

finally:
    print("success")

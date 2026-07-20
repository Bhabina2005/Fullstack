product_price = 5000
delivery_charges = 100
total = product_price + delivery_charges
print(total)

a = 30
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Assignment operators
followers = 1000
followers = followers + 100
print(followers)
followers = followers - 100
print(followers)

# Comparison operators
saved_password = "123@!abcde"
entered_password = "123@!abcde"
print(saved_password == entered_password)
print(saved_password != entered_password)
print(saved_password > entered_password)
print(saved_password < entered_password)
print(saved_password >= entered_password)
print(saved_password <= entered_password)

#Logical operators
balance = 1000
pin_code = True
if balance >= 1000 and pin_code:
    print("Withdrawal successful.")
else:
    print("Withdrawal failed.")


n = input("Enter the product name :")
price = float(input("Enter the price of the product"))
quantity = int(input("Enter the quantity of the product"))
discount = int(input("Enter the discount price"))
total = price * quantity - discount
final_bill = total
print("Product Name:", n)
print("Total Amount:", final_bill)

#conditional statements

password = input("Enter the password :")
if password == "admin@123":
    print("Welcome ")
else:
    print("Invalid password")

age  = 20
if age >=18:
    print("You are eligible to vote")

marks = int(input("Enter your marks:"))
if marks >= 90:
    print("10 Gadepoints")
elif marks >= 80 and marks <= 90:
    print("9 gradepoints")
elif marks >= 70 and marks <= 79:
    print("8 gradepoints")
elif marks >= 60 and marks <= 69:
    print("7 gradepoints")
elif marks >= 50 and marks <= 59:
    print("6 gradepoints")
else:
    print("You have failed the exam.")

#Logical operators

#And operator
age = 30
salary = 50000
if age >= 18 and salary >= 30000:
    print("You are eligible for the loan.")

#Or operator
day = "sunday"
if day == "sunday" or day == "saturday":
    print("Holiday")

#Not operator
is_student = False
print( not is_student)

login =False
if not login:
    print("Please login to continue.")

def withdrawal():
    Total_amount = 1000
    pin = 1234
    n = int(input("Enter the pin :"))
    if n == pin:
        withdraw = int(input("enter the amount to withdraw: "))
        if withdraw > Total_amount:
            print("Insufficient Balance")
        else:
            Balance_amount = Total_amount - withdraw
            print("Withdrawal successful.")
            print("Balance_amount:", Balance_amount)

    else:
        print("Invalid pin")


withdrawal()


#lOOPS
#for loop
for i in range(5):
    print("Sending mail")

users = ["Hi", "Hello", "Hai"]
for user in users:
    print("Sending mail to", user)

for i in range(1, 6):
    print(i)

name = "dhoni"
for ch in name:
    print(ch)

#while loop
i = 4
while i <= 20:
     print(i)
     i += 18


#continue statements
for i in range(10):
    if i == 3:
        continue
    print(i)

# break statements
for i in range(10):
    if i == 3:
        break
    print(i)

password = ""
while password != "admin@123":
    password = input("Enter the password :")
print("login successful")


students = ["Books", "Pens", "Pencils", "Notebooks", "Eraser"]
students.append("Sharpener")
students.remove("Pens")
students.insert(2, "Ruler")
print(students)



students=[]
while True:
    print("""
1 Add Student
2 View Students
3 Search Student
4 Exit
""")
    choice=input("Enter option: ")
    if choice=="1":
        name=input("Name: ")
        age=input("Age: ")
        course=input("Course: ")
        student={
        "name":name,
        "age":age,
        "course":course
        }
        students.append(student)
        print("Student Added Successfully")
    elif choice=="2":
        for student in students:
            print(student)
    elif choice=="3":
        search=input("Enter name: ")
        for student in students:
            if student["name"]==search:
                print(student)
    elif choice=="4":
        break
    else:
        print("Wrong Option")
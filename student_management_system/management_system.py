

import json


students = {}




def save_to_file():
    with open("student.json","w") as file:
        json.dump(students, file, indent=4)


def load_data():
    with open("student.json", "r") as file:
        global students
        students = json.load(file)

def add_student():
   name = input("enter student name:\t")
   age = int(input("enter student age:\t"))
   grade = input("enter student grade:\t")
   students[name]={
       "age": age,
       "grade": grade,
   }
   save_to_file()


def view_all_student():
    if not students:
        print("/n no student found on this record")
    else:
        print("/n--- student records ---")
        print("Name | Age | Grade")
        print("-" * 20)

        
        for name,info in students.items():
            print(f"{name} {info["age"]} {info["grade"]}")

def update_student(): 
    student_name = input("Enter student to update\t")
    if student_name not in students:
        print(f"Student Not Found !!!!!!!!!  -> {student_name}") 
    else:
        age = int(input("Enter new age"))
        grade = input("Enter Student Grade")

        temp_age=students[student_name]["age"]
        temp_grade=students[student_name]["grade"]


        if not age:
            age = temp_age
        if not grade:
            grade = temp_grade

        students [student_name] ["age"] = age
        students [student_name] ["grade"] = grade

        save_to_file()            


def delete_student():
    student_name = input("Enter student name to delete:\t")
    if not student_name in students:
        print("Student not found !!!!!!!!!!")

    else:
        yn = input(f"Are you sure you want to delete {student_name}? [y/n]").lower()
        if yn =="y":
          del students[student_name]
          print(f"{student_name} deleted from the system")
          save_to_file() 


        else:
            print("user not deleted")

        

while True:
 def main_menu():
    load_data()
    print("\n===============STUDENT MANAGEMENT SYSTEM================\n")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    user_choice=int(input("\nEnter options from 1 to 5:\t"))
    if (user_choice == 1):
       add_student()
    elif (user_choice == 2):
        view_all_student()
    elif (user_choice == 3):
        update_student()
    elif (user_choice == 4):
        delete_student()
    else:
        print("Exit")  


 break         


main_menu()    
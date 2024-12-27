print("=== Enter the student info ===")
name = input("enter the name: ")

social = int(input("enter the marks of social "))
science = int(input("enter the marks of science "))
english = int(input("enter the marks of english "))

total = sum([social,science,english])
average = total/2

print(f"{name}!! \n your total marks is: {total} and \n your average marks is:{average}")
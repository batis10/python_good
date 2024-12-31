students = []

student1 = {
    "name": "Alice", 
    "age": "15",
    "major": "math",
    }
student2 = {
    "name": "Bob", 
    "age": "16",
    "major": "science",
    }


students.append(student1)
students.append(student2)


for student in students:
    print( f"Name -> {student["name"]} Age -> {student["age"]} Major -> {student["major"]}" )

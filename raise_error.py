def check_age(age:int):
    if age<0:
        raise ValueError("age cannot be negative")
    if age>100:
       raise ValueError("age cannot be more than 100")
       
    return age

try:
 age = check_age(101)
 print(f"your age is {age}")
except ValueError as error:
   print(f"{error} : please enter the valid age frpm 1 - 100 ") 

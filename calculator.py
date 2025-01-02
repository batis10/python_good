def add(a, b):
    return a+b

def mult(a, b):
    return a * b

def div(a, b):
    if b ==0:
        print("cant div by 0")
    else:
     return a / b

def sub(a, b):
    return a - b    

def main():
    operator=input("enter the operator")
    a=1
    b=2

    if operator=="+":
        print(f"sum is {add(a,b)}")
    if operator=="-":    
        print(f"diff is {sub(a,b)}")
    if operator=="*":    
        print(f"product is {mult(a,b)}")
    if operator=="/":    
        print(f"value is {div(a,b)}")

main()        
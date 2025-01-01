def calculate_area(length: int = 0, breath: int = 0) -> int:
    return length * breath


def main():
    length = int(input("enter the length of rectangle: \t"))
    breath = int(input("enter the breath of rectangle: \t"))
    area = calculate_area(length=length, breath=breath)

    print("the area of rectangle with length {length} and breath {breath} is {area}")


main()   
    
    

class Student:

    no_of_student = 0


    def __init__(self, name, roll_no, reg_no):
        self.name = name
        self.roll_no = roll_no
        self.__reg_no = reg_no
        Student.no_of_student += 1

    @property
    def reg_no(self):
        return self.__reg_no  

    @reg_no.setter
    def reg_no(self, value):
        self.__reg_no = value

    def get_reg_no(self):
        return self.__reg_no      

    @classmethod
    def get_total_student(cls):
        print(cls.is_school_day("monday"))
        return cls.no_of_student 
    
    @staticmethod
    def is_school_day(day: str):
        if day.lower() != "saturday":
            return True
        else:
            False

ram = Student("ram", 4, "12345")  
print(ram.reg_no) 
user_reg_no = input("enter your reg no\t")
print(ram.reg_no)         
    


print(Student.get_total_student())
print(Student.is_school_day("monday"))


       
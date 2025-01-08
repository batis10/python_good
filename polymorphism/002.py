class Car:
    def __init__(self, brand, no_of_seats):
        self.brand = brand
        self.no_of_seats = 4
    

class ElectricCar(Car):
    def __init__(self, brand, no_of_seats):
        super().__init__(brand, no_of_seats)


    def Fuel_type(self):
        return "petrol or disel"

    def Fuel_type(self):
        return "battery"
    
            
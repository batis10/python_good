class Object:
     def __init__(self, weight, made_up_of):
          self.weight = weight
          self.made_up_of = made_up_of
          





class Car:
    def __init__(self, brand, model, color):
        self.color = color
        self.brand = brand
        self.model = model
        print(color, brand, model)


    def drive(self):
         return f"{self.brand} Car is running"    


class ElectricCar(Car):
       def __init__(self, range, brand, model, color, weight, made_up_of):
            super().__init__(brand, model, color)
            Object.__init__(self, weight, made_up_of)
            self.range = range 


tesla = ElectricCar(brand="Tesla", model="Model Y", color="Red", range="200km", weight=2000, made_up_of="metal")
tesla_weight = tesla.weight
tesla_drive = tesla.drive()
print(tesla_drive)

print(tesla.weight)
my_car = Car(brand="Toyota", model="Corolla", color="Grey")               
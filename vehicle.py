class Vehicle:
    def __init__(self, brand, speed):

        self.brand=brand
        self.speed=speed

    def display_info(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def display_car_info(self):
        print(f"Fuel Type: {self.fuel_type}")    

cr=Car("Toyota", 180, "Petrol")
cr.display_info()   
cr.display_car_info()
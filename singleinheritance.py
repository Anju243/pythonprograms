# Parent Class (Superclass)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

# Child Class (Subclass) inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, car_type):
        # Call the parent class constructor
        super().__init__(brand, model)
        self.car_type = car_type

    def display_car_info(self):
        # Call the display_info method from the parent class
        self.display_info()
        print(f"Car Type: {self.car_type}")

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", "Sedan")

# Call the method from the Car class
my_car.display_car_info()


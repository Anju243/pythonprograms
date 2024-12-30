# Grandparent Class (Superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Parent Class inherits from Animal
class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)  # Call the constructor of Animal class
        self.fur_color = fur_color

    def display_fur(self):
        print(f"{self.name} has {self.fur_color} fur.")

# Child Class inherits from Mammal
class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)  # Call the constructor of Mammal class
        self.breed = breed

    def display_breed(self):
        print(f"{self.name} is a {self.breed} breed.")

# Create an instance of the Dog class
dog = Dog("Buddy", "golden", "Golden Retriever")

# Call methods from the Dog class and its ancestors
dog.speak()  # Method from Animal class
dog.display_fur()  # Method from Mammal class
dog.display_breed()  # Method from Dog class

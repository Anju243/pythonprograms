# Parent Class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Parent Class 2
class Bird:
    def __init__(self, color):
        self.color = color

    def fly(self):
        print(f"{self.color} bird is flying.")

# Child Class inherits from both Animal and Bird
class Parrot(Animal, Bird):
    def __init__(self, name, color):
        # Call the constructors of both parent classes
        Animal.__init__(self, name)
        Bird.__init__(self, color)

    def display_info(self):
        print(f"{self.name} is a {self.color} parrot.")

# Create an instance of the Parrot class
parrot = Parrot("Polly", "green")

# Call methods from both parent classes
parrot.speak()        # Method from Animal class
parrot.fly()          # Method from Bird class
parrot.display_info() # Method from Parrot class

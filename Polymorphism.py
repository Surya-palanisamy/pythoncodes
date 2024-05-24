# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class (Child)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Another derived class (Child)
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Function demonstrating polymorphism
def make_animal_speak(animal):
    print(animal.speak())

# Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Using polymorphism to call the speak method
make_animal_speak(dog)  # Output: Buddy says Woof!
make_animal_speak(cat)  # Output: Whiskers says Meow!

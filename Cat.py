# Python program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

# Class for Cat
class Cat:

    # Class variable
    animal = "cat"

    # the init method or constructor
    def __init__(self, breed, color):
        # instance variable
        self.breed = breed
        self.color = color


jiba = Cat("tiger", "striped")
simba = Cat("lion", "brown")

print("jiba details:")
print("jiba is a ", jiba.animal)
print("breed: ", jiba.breed)
print("color: ", jiba.color)

print("\nSimba details: ")
print("simba is a ", simba.animal)
print("breed: ", simba.breed)
print("color: ", simba.color)

# class variables can be accessed using class
# name also

print("\nAccessing class variable using class name")
print(Cat.animal)

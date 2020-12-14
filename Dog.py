# Python program to
# demonstrate instantiating
# a class

class Dog:
    # A simple class attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def saystuff(self):
        print("I am a ", self.attr1)
        print("of type ", self.attr2)


# object instantiation
roger = Dog()

# access object attributes
print(roger.attr1)

# access object function
roger.saystuff()

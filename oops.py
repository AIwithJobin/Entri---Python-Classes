 # Define a simple Car class
class Car:
    # Class attribute or features or data members
    make = "Toyota"
    model = "Corolla"
    year = 2020

    # Method/fn to display car details
    def display_info(self):# self in a fn which creates instances
        print(self.make,self.year,self.model)

    def display_info_2(self,User_name):# self in a fn which creates instances
        print(self.make,self.year,self.model)
        print("Name of the user is:",User_name)

# Create an object of Car class
car_1 = Car()
car_2 = Car()

# print(car_1.model,car_2.make)
# car_1.display_info()

# car_2.display_info_2("Marco")


# Call the method to display car details
# car1.display_info()  # Output: 2020 Toyota Corolla

# __init__ method
import math

class Circle:
    # The __init__ method initializes the radius attribute for each object
    def __init__(self, radius):
        self.radius_1 = radius
        print("Inside __init__: self =", self)

    def find_area(self):
        area = math.pi * (self.radius_1 ** 2)
        print("Inside find_area: self =", self)
        return area

    def find_perimeter(self):
        perimeter = 2 * math.pi * self.radius_1
        print("Inside find_perimeter: self =", self)
        return perimeter

# Creating an object of the Circle class with a specific radius
my_circle = Circle(5)

# Calling the methods and printing the results
area = my_circle.find_area()
perimeter = my_circle.find_perimeter()

print(f"Area of the circle with radius {my_circle.radius_1} is: {area}")
print(f"Perimeter of the circle with radius {my_circle.radius_1} is: {perimeter}")



 # instance and class variables
class Dog:
    # Class variable
    species = "Canis lupus"  # All dogs are of the same species

    def __init__(self, name, age):
        # Instance variables
        self.name = name  # Unique to each instance
        self.age = age    # Unique to each instance

    def species_check(self):
        print("Species is: ",self.species)

# Creating two objects (instances) of Dog
dog1 = Dog("Buddy", 5)
dog2 = Dog("Charlie", 3)

# Accessing instance variables
print(dog1.name,dog1.age)  # Output: Buddy
print(dog2.name)  # Output: Charlie

# Accessing class variable
print(dog1.species)  # Output: Canis lupus
print(dog2.species)  # Output: Canis lupus

# Modifying the class variable
Dog.species = "Canis familiaris"

print(dog1.species)  # Output: Canis familiaris (reflects in all instances)
print(dog2.species)  # Output: Canis familiaris
# #
# Overriding a Class Variable with an Instance Variable
dog1.species = "Unknown species"  # Overrides the class variable for dog1 only
# # #
print(dog1.species)  # Output: Unknown species
print(dog2.species)  # Output: Canis familiaris

dog1.species_check()

# Muhammad Haroon Nasir
# 05/09/25
# Problem 6: This program defines a Car class with multiple attributes such as model, year, color, type, and manufacturer. It includes methods to 
# retrieve each attribute and display the full specifications of the car.

class car:

    def __init__(self, model, year, color, type_, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type_
        self.manufacturer = manufacturer

    # Methods to get individual attributes
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
    def get_color(self):
        return self.color
    
    def get_type(self):
        return self.type
    
    def get_manufacturer(self):
        return self.manufacturer
    
    # Method to return full specifications
    def fullspecs(self):
        return f"{self.model} {self.year} {self.color} {self.type} {self.manufacturer}"

# Creating car objects
car1 = car("Sports", 2012, "Blue", "Coupe", "Toyota")
car2 = car("Sedan", 2020, "Black", "Saloon", "Honda")

# Printing attributes using methods
print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.get_type())
print(car2.get_manufacturer())

# Printing full specifications
print(car1.fullspecs())
print(car2.fullspecs())
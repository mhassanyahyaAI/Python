def add(v1,v2):
    return v1+v2

def sub(v1,v2):
    return v1-v2

def squareroot(v1):
    return v1**(1/2)

class Car():
    """A simple attempt to represent a car."""
    
    # Attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    # Behavoiurs     
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title() 
    
    def read_odometer(self):        
        print("This car has " + str(self.odometer_reading) + " miles on it.")            
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage        
        else:            
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
class ElectricCar():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
   
    def get_descriptive_name(self):
        long_name = "Electric Car"+str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

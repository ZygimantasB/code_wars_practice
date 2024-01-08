# OOP Exercise 1: Create a Class with instance attributes

class Vehicle1:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


vehicle = Vehicle1(max_speed=10, mileage=500)

print(vehicle.max_speed)
print(vehicle.mileage)

# OOP Exercise 2: Create a Vehicle class without any variables and methods

class Vehicle2:
    pass

# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max

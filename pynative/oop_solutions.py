# OOP Exercise 1: Create a Class with instance attributes

class CarInformation:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


modelX = CarInformation(240, 240)
# print(modelX.max_speed, modelX.mileage)


# OOP Exercise 2: Create a Vehicle class without any variables and methods


class Vehicle:
    pass


# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class


class Vehicle3:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle3):
    pass


school_bus = Bus('Volvo', 180, 12)


print('Vehicle Name:', school_bus.name, 'Car max speed:', school_bus.max_speed, 'Mileage', school_bus.mileage)

# OOP Exercise 4: Class Inheritance

class Vehicle4:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle4):

    def seating_capacity(self, capacity: int=50):
        return super().seating_capacity(capacity=50)

# OOP Exercise 5: Define a property that must have the same value for every class instance (object)


class Vehicle5:

    color = 'White'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus5(Vehicle5):
    pass


class Car5(Vehicle5):
    pass

# OOP Exercise 6: Class Inheritance

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
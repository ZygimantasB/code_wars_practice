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
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f'Car: {self.name} and cars max speed {self.max_speed} and mileage {self.mileage}'


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, stops):
        super().__init__(name, max_speed, mileage)
        self.stops = stops

    def __str__(self):
        stops_str = ', '.join(self.stops)
        return f'Bus {self.name}, {self.max_speed} and {self.mileage} and bus stops: {stops_str}'


bus = Bus('BMW', 33, 999, ['Vilnius', 'Kaunas', 'Palanga'])


# print(bus)

# OOP Exercise 4: Class Inheritance

class Vehicle4:

    def __init__(self, name: str, max_speed: int, mileage: int, capacity: int = 50) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self) -> str:
        return f'The seating capacity of a {self.name} is {self.capacity} passengers'


vehicle4 = Vehicle4('Volvo', 99, 999, 20)
print(vehicle4.seating_capacity())

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


bus5 = Bus5('Audi', 99, 100000)
print(bus5.color, bus5.name, bus5.mileage, bus5.mileage)

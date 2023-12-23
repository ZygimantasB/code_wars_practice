# Exercise 1: Create a function in Python
from typing import List, Tuple


def print_name_age(name: str, age: int) -> tuple[str, int]:
    return name, age


# print(print_name_age('James', 23))


# Exercise 2: Create a function with variable length of arguments

def func1(*args: str) -> None:
    print('Printin values')
    for number in args:
        print(number, end='\n')


# func1(20, 40, 60)
# func1(80, 100)


# Exercise 3: Return multiple values from a function

def calculation(a: int, b: int) -> list[int]:
    additional = a + b
    substation = a - b
    return [additional, substation]


# print(calculation(40, 10))

def show_employee(name: str, salary: int = 9_000) -> str:
    return f'Name: {name} salary: {salary}'


# print(show_employee('Ben', 12_000))
# print(show_employee('Jessa',))

# Exercise 5: Create an inner function to calculate the addition in the following way


def outer_function(a: int, b: int) -> int:
    def additional() -> int:
        return a + b
    return additional() + 5


# print(outer_function(5, 10))

# Exercise 6: Create a recursive function

def recursive_sum(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)


# print(recursive_sum(10))

# Exercise 7: Assign a different name to function and call it through the new name


def display_student(name, age):
    print(name, age)


show_student = display_student


show_student("Emma", 26)


# Exercise 8: Generate a Python list of all the even numbers between 4 to 30


def generate_even_list(start_number: int, end_number: int) -> list[int]:
    return [number for number in range(start_number, end_number + 1) if number % 2 == 0]


# print(generate_even_list(4, 30))


# Exercise 9: Find the largest item from a given list
def find_largest_number(*args):
    max_number = 0
    for number in args:
        if number > max_number:
            max_number = number
    return max_number


x = [4, 6, 8, 24, 12, 2]
print(find_largest_number(*x))


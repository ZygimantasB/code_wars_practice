# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
# Exercise 1: Print First 10 natural numbers using while loop

def print_number_in_range(start_index, end_index):
    # return [number for number in range(start_index, end_index + 1)]
    for number in range(start_index, end_index + 1):
        print(number, end='\n')


# print_number_in_range(start_index=1, end_index=10)

# Exercise 2: Print the following pattern

# for number1 in range(1, 6):
#     for number2 in range(1, number1 + 1):
#         print(number2, end=' ')
#     print()

# Exercise 3: Calculate the sum of all numbers from 1 to a given number


def sum_number_of_sequence(numbers):
    return sum([number for number in range(1, numbers + 1)])
    # return numbers * (numbers + 1) // 2


# print(sum_number_of_sequence(55))


# Exercise 4: Write a program to print multiplication table of a given number


def print_multiplication_table(number):
    for num in range(1, 10 + 1):
        print(num * number)


# print_multiplication_table(2)

# Exercise 5: Display numbers from a list using loop

numbers = [12, 75, 150, 180, 145, 525, 50]

def display_numbers(example_list):
    result = []
    for number in example_list:
        if number > 500:
            break
        elif number > 150:
            continue
        elif number % 5 == 0:
            result.append(number)
    return result


# print(display_numbers(numbers))


# Exercise 6: Count the total number of digits in a number

def count_digits(number):
    return len(str(number))


# print(count_digits(75869))

# Exercise 8: Print list in reverse order using a loop

def reverse_list(my_list):
    # return my_list[::-1]
    return [number for number in reversed(my_list)]


list1 = [10, 20, 30, 40, 50]

# print(reverse_list(list1))

# Exercise 9: Display numbers from -10 to -1 using for loop


def display_negative_number(start_index, end_index):
    for number in range(-start_index, -end_index):
        print(number)


# display_negative_number(10, 1)

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop

def use_else_block():
    for i in range(5):
        print(i)
    else:
        print('Done!')


# use_else_block()

# Exercise 11: Write a program to display all prime numbers within a range

def is_prime_number(start_number, end_number):
    for number in range(start_number, end_number + 1):
        if number > 1:
            for number2 in range(2, number):
                if (number % number2) == 0:
                    break
            else:
                print(number)


# is_prime_number(25, 50)

# Exercise 12: Display Fibonacci series up to 10 terms

def show_fibonacci(number_range):
    previous_number, next_number = 0, 1
    for _ in range(number_range):
        print(previous_number, end=' ')
        result = previous_number + next_number
        next_number = previous_number
        previous_number = result

# show_fibonacci(20)

# Exercise 13: Find the factorial of a given number

import math


def find_factorial(number_range):
    # result = 1
    # for number in range(1, factorial_number + 1):
    #     result *= number
    # return result
    # return [math.factorial(number) for number in range(1, number_range + 1)]
    factorial = 1
    for i in range(1, number_range + 1):
        factorial *= i
    return factorial


# print(find_factorial(number_range=5))

# Exercise 14: Reverse a given integer number


def reverse_given_number(user_number):
    result = str(user_number)[::-1]
    return int(result)


# print(reverse_given_number(76542))

# Exercise 15: Use a loop to display elements from a given list present at odd index positions


def print_odd_numbers(user_list):
    # result = []
    # for number in range(1, len(user_list) + 1, 2):
    #     result.append(user_list[number])
    # return result
    return [user_list[index] for index in range(1, len(user_list) + 1, 2)]


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# print(print_odd_numbers(my_list))


# Exercise 16: Calculate the cube of all numbers from 1 to a given number


def print_number_qube(start_number, end_number):
    for number in range(start_number, end_number + 1):
        print(f'Current number is : {number} and the Cube is {number ** 3}')


# print_number_qube(1, 6)


# Exercise 17: Find the sum of the series upto n terms


def sum_sequence_numbers(numbers_range):
    str_result = ''
    result = 0
    for _ in range(1, numbers_range + 1):
        str_result += '2'
        result += int(str_result)
    return result


# print(sum_sequence_numbers(5))


# Exercise 18: Print the following pattern

def print_star_pattern(n):
    # First, print the upper part of the pattern
    for i in range(n):
        print('* ' * (i+1))

    # Then, print the lower part of the pattern
    for i in range(n-1, 0, -1):
        print('* ' * i)


print_star_pattern(5)

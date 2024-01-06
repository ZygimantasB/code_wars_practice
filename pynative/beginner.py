# https://pynative.com/python-basic-exercise-for-beginners/
# Exercise 1: Calculate the multiplication and sum of two numbers
# def number_multiplayer(number1, number2):
#     product = number1 * number2
#     if product <= 1000:
#         return product
#     else:
#         return number1 + number2

def number_multiplayer(number1, number2):
    try:
        product = number1 * number2
        if product <= 1000:
            result = product
        else:
            result = number1 + number2
        return result
    except TypeError:
        return 'Invalid input: Both arguments must be integers'
    except Exception as error:
        return f"An error occurred: {error}"
    finally:
        print('Execution completed i number_multiplayer')


# print(number_multiplayer(20, 30))
# print(number_multiplayer(40, 30))
# print(number_multiplayer('a', 30))

# Exercise 2: Print the sum of the current number and the previous number


def print_previous_number(numbers):
    previous_number = 0
    for current_number in range(numbers):
        sum_numbers = previous_number + current_number
        print(f"Current Number {current_number} Previous Number Sum: {sum_numbers}")
        previous_number = current_number


# print_previous_number(10)

# Exercise 3: Print characters from a string that are present at an even index number


def second_n_value(list_values) -> list[int]:
    if not isinstance(list_values, list):
        raise TypeError('Input must be a list')

    if len(list_values) == 0:
        raise ValueError('List cannot be empty')

    if not all(isinstance(item, int) for item in list_values):
        raise ValueError('All elements must be on integers')

    return [value for index, value in enumerate(list_values) if index % 2 == 0]


# print(second_n_value([1, 2, 3, 4]))
# print(second_n_value([1, 'a', 3, 4]))
# print(second_n_value(None))
print(second_n_value(1))


def second_n_value1(values):
    for index, value in enumerate(values):
        if index % 2 == 0:
            print(value)


# print(second_n_value('pynative'))
# second_n_value1('pynative')

# Exercise 4: Remove first n characters from a string


def remove_strings(word, value_remove):
    return word[value_remove:]


# print(remove_strings('pynative', 4))

# Exercise 5: Check if the first and last number of a list is the same


def is_palindrome(numbers_list):
    return numbers_list[0] == numbers_list[-1]


# print(is_palindrome([10, 20, 30, 40, 10]))
# print(is_palindrome([75, 65, 35, 75, 30]))

# Exercise 6: Display numbers divisible by 5 from a list


def divisible_by_five(numbers):
    return [number for number in numbers if number % 5 == 0]


# print(divisible_by_five([10, 20, 33, 46, 55]))

# Exercise 7: Return the count of a given substring from a string


def count_emma(sentence, name):
    # return sum(1 for value in sentence.split() if value == name)
    return f'Emma appeared {sentence.count(name)} times'


str_x = "Emma is good developer. Emma is a writer"


# print(count_emma(sentence=str_x, name='Emma'))

# Exercise 8: Print the following pattern


def print_following_pattern(numbers):
    for number1 in range(1, numbers + 1):
        print(' '.join(str(number1) for _ in range(number1)))


# print_following_pattern(5)

# Exercise 9: Check Palindrome Number


def is_palindrome_number(number):
    is_palindrome1 = 'Yes. given number is palindrome number'
    not_palindrome = "No. given number is not palindrome number"
    return is_palindrome1 if str(number) == str(number)[::-1] else not_palindrome


# print(is_palindrome_number(454))
# print(is_palindrome_number(123))
# print(is_palindrome_number(898))
# print(is_palindrome_number(8989854))

# Exercise 10: Create a new list from two list using the following condition


def create_odd_even_list(num_list1, num_list2):
    # odd_even_list = []
    # odd_even_list.extend([odd_number for odd_number in num_list1 if odd_number % 2 != 0])
    # odd_even_list.extend([even_number for even_number in num_list2 if even_number % 2 == 0])
    # return odd_even_list
    return ([odd_number for odd_number in num_list1 if odd_number % 2 != 0] \
            + [even_number for even_number in num_list2 if even_number % 2 == 0])


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# print(create_odd_even_list(list1, list2))

# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.


def reverse_digit(numbers):
    return ' '.join(str(numbers)[::-1])


# print(reverse_digit(7536))

def calculate_taxes(income):
    tax = 0
    if income > 10_000:
        income -= 10_000
        if income > 10_000:
            tax += 10_000 * 0.1
            income -= 10_000
        else:
            tax += income * 0.1
            income = 0
    if income > 0:
        tax += income * 0.2
    return tax


# print(calculate_taxes(45_000))


# Exercise 13: Print multiplication table from 1 to 10

def create_multiplication_table(numbers):
    for number1 in range(1, numbers + 1):
        for number2 in range(1, numbers + 1):
            print(number1 * number2, end=' ')
        print()


# create_multiplication_table(10)

# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)

def print_asterix_backwards():
    for j in range(6, 0, -1):
        print(" *" * j)


# print_asterix_backwards()

# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

from math import pow

# def exponent():
#     repeat = 'yes'
#     while repeat == 'yes':
#         base = int(input('Base number: '))
#         exponent = int(input('Exponent number: '))
#         print(pow(base, exponent))
#
#         repeat = input('Do you want to repeat: ')
#         if repeat == 'no':
#             break


def exponent(base, exp):
    return f'{base} raises top the power of {exp} is: {int(pow(base, exp))}'

#
# print(exponent(2, 5))
# print(exponent(5, 4))

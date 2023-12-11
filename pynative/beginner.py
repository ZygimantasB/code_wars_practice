# https://pynative.com/python-basic-exercise-for-beginners/
# Exercise 1: Calculate the multiplication and sum of two numbers
def number_multiplayer(number1, number2):
    product = number1 * number2
    if product <= 1000:
        return product
    else:
        return number1 + number2


# print(number_multiplayer(20, 30))
# print(number_multiplayer(40, 30))

# Exercise 2: Print the sum of the current number and the previous number

def print_previous_number(numbers):
    previous_number = 0
    for current_number in range(numbers):
        sum_numbers = previous_number + current_number
        print(f"Current Number {current_number} Previous Number Sum: {sum_numbers}")
        previous_number = current_number


# print(print_previous_number(10))

# Exercise 3: Print characters from a string that are present at an even index number

def second_n_value(values):
    return [value for index, value in enumerate(values) if index % 2 == 0]


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

print(count_emma(sentence=str_x, name='Emma'))

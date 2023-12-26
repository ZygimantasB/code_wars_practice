# Exercise 1A: Create a string made of the first, middle and last character

def create_string(word):
    return word[0] + word[(len(word) // 2)] + word[-1]


# print(create_string('James'))

# Exercise 1B: Create a string made of the middle three characters

def middle_three_chars(s):
    # Find the length of the string
    length = len(s)

    # Calculate the starting index for the middle three characters
    start_index = length // 2 - 1

    # Extract and return the middle three characters
    return s[start_index:start_index + 3]

# Test the function with the given cases
str1 = "JhonDipPeta"
# print("Case 1 Output:", middle_three_chars(str1))

str2 = "JaSonAy"
# print("Case 2 Output:", middle_three_chars(str2))

# Exercise 2: Append new string in the middle of a given string


def append_string_middle(first_word, second_word):
    mid_index = len(first_word) // 2
    return first_word[:mid_index] + second_word + first_word[mid_index:]


# print(append_string_middle("Ault", "Kelly"))

# Exercise 3: Create a new string made of the first, middle, and last characters of each input string


def create_string(first_word, second_word):
    first_combination = first_word[0] + second_word[0]
    middle_combination = first_word[len(first_word) // 2] + second_word[len(second_word) // 2]
    last_combination = first_word[-1] + second_word[-1]
    return first_combination + middle_combination + last_combination


# print(create_string("America", "Japan" ))


def lowercase_first(word):
    lower_case = ''
    upper_case = ''
    for char in word:
        if char.islower():
            lower_case += char
        else:
            upper_case += char
    return lower_case + upper_case


# print(lowercase_first('PyNaTive'))

# Exercise 5: Count all letters, digits, and special symbols from a given string

from string import punctuation

def count_letters(symbol_sequence):
    # return {char: symbol_sequence.count(char) for char in set(symbol_sequence)}
    # count_dict = {'Chars': 0, 'Symbols': 0, 'Digits': 0}
    # for char in symbol_sequence:
    #     if char.isalpha():
    #         count_dict['Chars'] += 1
    #     elif char.isdigit():
    #         count_dict['Digits'] += 1
    #     # elif not char.isalpha() and not char.isdigit():
    #     # elif char in punctuation:
    #     else:
    #         count_dict['Symbols'] += 1
    # return count_dict
    count_dict = {
        'Char': sum(char.isalpha() for char in symbol_sequence),
        'Digits': sum(char.isdigit() for char in symbol_sequence),
        'Symbols': sum(char in punctuation for char in symbol_sequence)
    }
    return count_dict


str1 = "P@#yn26at^&i5ve"

# print(count_letters(str1))


# Exercise 6: Create a mixed String using the following rules

def mix_strings(s1, s2):
    # Initialize the result string
    s3 = ""

    # Loop through the strings
    for i in range(max(len(s1), len(s2))):
        # Add character from s1 if available
        if i < len(s1):
            s3 += s1[i]

        # Add character from s2 in reverse order if available
        if i < len(s2):
            s3 += s2[-(i+1)]

    return s3

# Given strings
s1 = "Abc"
s2 = "Xyz"

# Expected Output
# print("Expected Output:", mix_strings(s1, s2))

# Exercise 7: String characters balance Test


def is_string_balance(check_string, words):
    return any(True for _ in check_string if check_string in words)


# print(is_string_balance("Yn", "PYnative"))
# print(is_string_balance("Ynf", "PYnative"))


# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case


def count_occurrence(words, searching_word):
    return words.lower().count(searching_word.lower())


print(count_occurrence("Welcome to USA. usa awesome, isn't it?", 'USA'))


# Exercise 9: Calculate the sum and average of the digits present in a string


def count_digits(words):
    find_digits = [int(number) for number in words if number.isdigit()]
    sum_digits = sum(find_digits)
    average_digits = sum(find_digits) / len(find_digits)
    return sum_digits, average_digits


print(count_digits("PYnative29@#8496"))

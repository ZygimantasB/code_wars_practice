# Exercise 1: Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


def create_dict(keys1, values1):
    # return {key: value for key, value in zip(keys1, values1)}
    return dict(zip(keys1, values1))
    # combined_lists = (*keys1, *values1)
    # return combined_lists


# print(create_dict(keys, values))


# Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


def merge_two_dictionaries(sample_dict1, sample_dict2):
    # sample_dict1.update(sample_dict2)
    combined_dict = {**sample_dict1, **sample_dict2}
    return combined_dict


# print(merge_two_dictionaries(dict1, dict2))

# Exercise 3: Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# print(sampleDict['class']['student']['marks']['history'])


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Exercise 4: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}


def initialize_dictionary_values(sample_list, sample_dict):
    return dict.fromkeys(sample_list, sample_dict)


# print(initialize_dictionary_values(employees, defaults))

# Exercise 5: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]


def create_dictionary_from_keys(my_dict, extract_keys):
    return {key: my_dict[key] for key in extract_keys}


# print(create_dictionary_from_keys(sample_dict, keys))

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]


# Exercise 6: Delete a list of keys from a dictionary


def remove_keys(sample_dict1, remove_keys1):
    return {key: sample_dict1[key] for key in sample_dict1 if key not in remove_keys1}


# print(remove_keys(sample_dict, keys))

# Exercise 7: Check if a value exists in a dictionary

sample_dict7 = {'a': 100, 'b': 200, 'c': 300}


def check_insisting_value(my_sample_dict, checking_value):
    # return checking_value in my_sample_dict.values()
    # return any(value == checking_value for value in my_sample_dict.values())
    return checking_value in [value for value in my_sample_dict.values()]


# print(check_insisting_value(sample_dict7, '200'))
# print(check_insisting_value(sample_dict7, 200))


# Exercise 6: Delete a list of keys from a dictionary


keys6 = ["name", "salary"]

sample_dict6 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}


def delete_keys_from_dict(sample_dict, remove_keys):
    return {key: values for key, values in sample_dict.items() if key not in remove_keys}


# print(delete_keys_from_dict(sample_dict6, keys6))


# Exercise 7: Check if a value exists in a dictionary

sample_dict7 = {'a': 100, 'b': 200, 'c': 300}


def check_existing_value(price_dict, value):
    # return {f'{value} present in the dict' if value in price_dict.values()
    #         else f'{value} not present in the dict':
    #             value for key, value in price_dict.items()}
    # return value in price_dict.values()
    return f'{value} present in the dict' if value in price_dict.values() else False


# print(check_existing_value(sample_dict7, 200))
# print(check_existing_value(sample_dict7, 400))

# Exercise 8: Rename key of a dictionary

def rename_key_dict(my_dict, old_key, new_key):
    my_dict[new_key] = my_dict.pop(old_key)
    return my_dict


sample_dict8 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# print(rename_key_dict(sample_dict8, 'city', 'location'))

# Exercise 9: Get the key of a minimum value from the following dictionary

sample_dict9 = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}


def get_minimum_value(my_dict):
    return min(my_dict, key=my_dict.get)


print(get_minimum_value(sample_dict9))

# Exercise 10: Change value of a key in a nested dictionary

sample_dict10 = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}


def multiply_items_dictionary(dict_values, multiply_value):
    return {key: value * multiply_value for key, value in dict_values.items()}


# print(multiply_items_dictionary({'data1': 100, 'data2': -54, 'data3': 247}, 2))


# 13. Write a Python program to map two lists into a dictionary.
def combine_two_list_into_dict():
    keys = ['red', 'green', 'blue']
    values = ['#FF0000', '#008000', '#0000FF']
    return {key: value for key, value in zip(keys, values)}


# print(combine_two_list_into_dict())

# 14. Write a Python program to sort a given dictionary by key.
def sort_values_by_key():
    color_dict = {
        'red': '#FF0000',
        'green': '#008000',
        'black': '#000000',
        'white': '#FFFFFF'
    }
    return dict(sorted(color_dict.items(), key=lambda color: color[0]))


# print(sort_values_by_key())

# 15. Write a Python program to get the maximum and minimum values of a dictionary.

def get_max_min_values():
    my_dict = {'x': 500, 'y': 5874, 'z': 560}
    # sorted_values = sorted(my_dict.items(), key=lambda value: value[1])
    # return sorted_values[0], sorted_values[-1]
    # key_max = max(my_dict.items(), key=lambda max_value: max_value[0])
    # key_min = min(my_dict.items(), key=lambda min_value: min_value[0]
    key_max = max(my_dict.keys(), key=lambda max_value: my_dict[max_value])
    key_min = min(my_dict.keys(), key=lambda min_value: my_dict[min_value])
    return key_max, key_min

# print(get_max_min_values())

# 16. Write a Python program to get a dictionary from an object's fields.
class TestClass:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

def get_dict_from_object_fields():
    obj = TestClass('value1', 'value2', 'value3')
    return vars(obj)

# print(get_dict_from_object_fields())

# 17. Write a Python program to remove duplicates from the dictionary.

def remove_duplicates_from_dict():
    student_data = {
        'id1': {
            'name': ['Sara'],
            'class': ['V'],
            'subject_integration': ['english, math, science']
        },
        'id2': {
            'name': ['David'],
            'class': ['V'],
            'subject_integration': ['english, math, science']
        },
        'id3': {
            'name': ['Sara'],
            'class': ['V'],
            'subject_integration': ['english, math, science']
        },
        'id4': {
            'name': ['Surya'],
            'class': ['V'],
            'subject_integration': ['english, math, science']
        }
    }
    result = {}
    for key, value in student_data.items():
        if value not in result.values():
            result[key] = value

    return result


# print(remove_duplicates_from_dict())


# 18. Write a Python program to check if a dictionary is empty or not.
def check_is_dict_empty(dict_sample):
    # return False if  dict_sample else True
    # return len(dict_sample) == 0
    # return bool(dict_sample)
    return not dict_sample

# 19. Write a Python program to combine two dictionary by adding values for common keys.

def combine_dictionaries():
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    # d1.update(d2)
    # return d1
    for key, value in d2.items():
        if key in d1.items():
            d1[key] += value
        else:
            d1[key] = value
    return d1


# print(combine_dictionaries())

# 20. Write a Python program to print all distinct values in a dictionary.

def print_distinct_values():
    sample_data =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    # distinct_values = set(val for dic in sample_data for val in dic.values())
    unique_values = set(value for subdict in sample_data for value in subdict.values())

    return unique_values


# print(print_distinct_values())
#
# 22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
def find_3_highest_values():
    my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
    return sorted(my_dict.values())[-3:]

# print(find_3_highest_values())

# 23. Write a Python program to combine values in a list of dictionaries.
def combine_values():
    item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    result = {}
    for d in item_list:
        if d['item'] in result:
            result[d['item']] += d['amount']
        else:
            result[d['item']] = d['amount']
    return result

# print(combine_values())

# 24. Write a Python program to create a dictionary from a string.

def count_letters():
    sample_string = 'w3resource'
    # return {char: sample_string.count(char) for char in sample_string}
    result = {}
    for char in sample_string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

# print(count_letters())


# 26. Write a Python program to count the values associated with a key in a dictionary.
def count_values_associated_keys():
    student = [{'id': 1, 'success': True, 'name': 'Lary'},
               {'id': 2, 'success': False, 'name': 'Rabi'},
               {'id': 3, 'success': True, 'name': 'Alex'}]
    return sum(d['id'] for d in student), sum(d['success'] for d in student)


# print(count_values_associated_keys())

# 27. Write a Python program to convert a list into a nested dictionary of keys.
def dict_to_nested_list():
    number_list = [1, 2, 3, 4]
    nested_dict = {}
    for number in reversed(number_list):
        nested_dict = {number: nested_dict}
    return nested_dict


print(dict_to_nested_list())

# print(check_is_dict_empty({}))
# print(check_is_dict_empty({'Hello': 1}))

# sample_dict_test = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
#
# new_value = {key: 'key is even ' if key % 2 == 0 else 'odd' for key in sample_dict_test.items()}
# print(new_value)

# sample_dict_test = {'apple': 1, 'banana': 2, 'cherry': 3}
#
# new_dict = {key: 'fruit is 2' if value == 2 else 'fruit count is not 2' for key, value in sample_dict_test.items()}
# print(new_dict)

# sample_dict_test = {'apple': 3, 'banana': 2, 'cherry': 1}
#
# sorted_dict = dict(sorted(sample_dict_test.items(), key=lambda item: item[1]))
# print(sorted_dict)

# some_numbers = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7, 7]
#
# max_number = max(some_numbers)
# print(max_number)
# count_numbers = {number: some_numbers.count(number) for number in some_numbers}
# print(count_numbers[max_number])
#
# most_frequent_number = max(some_numbers, key=some_numbers.count)
# print(most_frequent_number)

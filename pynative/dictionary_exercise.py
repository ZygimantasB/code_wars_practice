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


print(remove_keys(sample_dict, keys))

# Exercise 7: Check if a value exists in a dictionary

sample_dict7 = {'a': 100, 'b': 200, 'c': 300}


def check_insisting_value(my_sample_dict, checking_value):
    # return checking_value in my_sample_dict.values()
    # return any(value == checking_value for value in my_sample_dict.values())
    return checking_value in [value for value in my_sample_dict.values()]

print(check_insisting_value(sample_dict7, '200'))
print(check_insisting_value(sample_dict7, 200))

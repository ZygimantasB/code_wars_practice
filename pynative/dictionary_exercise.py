# Exercise 1: Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


def create_dict(keys1, values1):
    # return {key: value for key, value in zip(keys1, values1)}
    return dict(zip(keys1, values1))
    # combined_lists = (*keys1, *values1)
    # return combined_lists


print(create_dict(keys, values))


# Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


def merge_two_dictionaries(sample_dict1, sample_dict2):
    # sample_dict1.update(sample_dict2)
    combined_dict = {**sample_dict1, **sample_dict2}
    return combined_dict


print(merge_two_dictionaries(dict1, dict2))

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

print(sampleDict['class']['student']['marks']['history'])


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Exercise 4: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}


def initialize_dictionary_values(sample_list, sample_dict):
    return dict.fromkeys(sample_list, sample_dict)


print(initialize_dictionary_values(employees, defaults))


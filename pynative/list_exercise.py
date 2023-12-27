# Exercise 1: Reverse a list in Python

def reverse_list(numbers_list):
    # return numbers_list[::-1]
    numbers_list.reverse()
    return numbers_list


# print(reverse_list([100, 200, 300, 400, 500]))


# Exercise 2: Concatenate two lists index-wise

def concat_two_lists(first_list, second_list):
    # return first_list + second_list
    # first_list.extend(second_list)
    combined_list = [*first_list, *second_list]
    return combined_list


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]


# print(concat_two_lists(list1, list2))


# Exercise 3: Turn every item of a list into its square

def print_square(numbers):
    return [number ** 2 for number in numbers]


# print(print_square([1, 2, 3, 4, 5, 6, 7]))

# Exercise 4: Concatenate two lists in the following order


def concat_list_order(first_list, second_list):
    return [first + second for first in first_list for second in second_list]


# print(concat_list_order(["Hello ", "take "], ["Dear", "Sir"]))


# Exercise 5: Iterate both lists simultaneously

def iterate_both_lists(list1, list2):
    reversed_list2 = list2[::-1]

    for item1, item2 in zip(list1, reversed_list2):
        print(item1, item2)


# iterate_both_lists([10, 20, 30, 40], [100, 200, 300, 400])

# Exercise 6: Remove empty strings from the list of strings


def remove_empty_string(my_list):
    return [word for word in my_list if word or word == 0]


print(remove_empty_string(["Mike", "", "Emma", "Kelly", "", "Brad"]))

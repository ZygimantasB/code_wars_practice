# Exercise 1: Add a list of elements to a set

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]


def add_element_set(old_set, new_set):
    old_set.update(new_set)
    return old_set


# print(add_element_set(sample_set, sample_list))

# Exercise 2: Return a new set of identical items from two sets


def return_identical_items(my_set1, my_set2):
    # result = set()
    # for number in my_set1:
    #     if number in my_set2:
    #         result.add(number)
    # return result
    # return {number for number in my_set1 if number in my_set2}
    return my_set1.intersection(my_set2)


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


# print(return_identical_items(set1, set2))

# Exercise 3: Get Only unique items from two sets


def return_unique_set(my_set1, my_set2):
    # return my_set1 | my_set2
    return my_set1.union(my_set2)


# print(return_unique_set(set1, set2))

# Exercise 4: Update the first set with items that don’t exist in the second set

def update_set(my_set1, my_set2):
    # return {number for number in my_set1 if number not in my_set2}
    my_set1.difference_update(my_set2)
    return my_set1


set14 = {10, 20, 30}
set24 = {20, 40, 50}


# print(update_set(set14, set24))

# Exercise 5: Remove items from the set at once


def remove_items_once(my_set1, *args):
    return {number for number in my_set1 if number not in args[0]}


numbers_list = [10, 20, 30]
set15 = {10, 20, 30, 40, 50}

# print(remove_items_once(set15, numbers_list))


# Exercise 6: Return a set of elements present in Set A or B, but not both


def return_present_element(my_set1, my_set2):
    # return my_set1.symmetric_difference(my_set2)
    return (my_set1 | my_set2) - (my_set1 & my_set2)


set16 = {10, 20, 30, 40, 50}
set26 = {30, 40, 50, 60, 70}

# print(return_present_element(set16, set26))

# Exercise 7: Check if two sets have any elements in common. If yes, display the common elements


def display_common_elements(my_set1, my_set2):
    return my_set1 & my_set2


set17 = {10, 20, 30, 40, 50}
set27 = {60, 70, 80, 90, 10}


# print(display_common_elements(set17, set27))


# Exercise 8: Update set1 by adding items from set2, except common items

def update_set1_common_items(my_set1, my_set2):
    result = ({number for number in my_set1 if number not in my_set2} |
                         {number for number in my_set2 if number not in my_set1})
    return result


set18 = {10, 20, 30, 40, 50}
set28 = {30, 40, 50, 60, 70}


# print(update_set1_common_items(set18, set28))

# Exercise 9: Remove items from set1 that are not common to both set1 and set2


def remove_common_values(my_set1, my_set2):
    return my_set1 & my_set2


set19 = {10, 20, 30, 40, 50}
set29 = {30, 40, 50, 60, 70}


print(remove_common_values(set19, set29))

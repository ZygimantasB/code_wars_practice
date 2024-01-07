# Exercise 1: Reverse the tuple

def reverse_tuple(my_tuple):
    return tuple(reversed(my_tuple))


tuple1 = (10, 20, 30, 40, 50)


# print(reverse_tuple(tuple1))

# Exercise 2: Access value 20 from the tuple

def excess_value_tuple(my_tuple):
    return my_tuple[1][1]


tuple12 = ("Orange", [10, 20, 30], (5, 15, 25))


# print(excess_value_tuple(tuple12))

# Exercise 3: Create a tuple with single item 50

def create_tuple(my_tuple):
    return tuple([my_tuple])


# print(create_tuple(50))


# Exercise 4: Unpack the tuple into 4 variables


tuple14 = (10, 20, 30, 40)

# number1, number2, number3, number4 = tuple14
# print(number1)
# print(number2)
# print(number3)
# print(number4)


# Exercise 5: Swap two tuples in Python

tuple15 = (11, 22)
tuple25 = (99, 88)

tuple25, tuple15 = tuple15, tuple25

# print(tuple15)
# print(tuple25)

# Exercise 6: Copy specific elements from one tuple to a new tuple

tuple16 = (11, 22, 33, 44, 55, 66)

# print(tuple16[3: 5])


# Exercise 7: Modify the tuple

tuple17 = (11, [22, 33], 44, 55)

tuple17[1][0] = 222
# print(tuple17)

# Exercise 8: Sort a tuple of tuples by 2nd item


def sort_2nd_element(my_tuple):
    return sorted(my_tuple, key=lambda number: number[1], reverse=True)


tuple18 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))


# print(sort_2nd_element(tuple18))


# Exercise 9: Counts the number of occurrences of item 50 from a tuple

def count_tuple_occurrences(my_tuple):
    result = {number: my_tuple.count(number) for number in my_tuple}
    sorted_result = sorted(result.items(), key=lambda number: number[1])
    return sorted_result


tuple19 = (50, 10, 60, 70, 50)


# print(count_tuple_occurrences(tuple19))


# Exercise 10: Check if all items in the tuple are the same


def check_values_same(my_tuple):
    return all(number == my_tuple[0] for number in my_tuple)


tuple110 = (45, 45, 45, 45)


print(check_values_same(tuple110))

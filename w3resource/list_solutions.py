# 1. Write a Python program to sum all the items in a list.
import ast
import itertools
from random import shuffle, choice
from itertools import groupby



class ListSolutions:

    def __init__(self):
        self.numbers_list = [1, 2, 3, 33, 4, 9, 10, 10]
        self.numbers_list1 = [1, 2, 3, 12, 13, 14, 15, 16, 17]
        self.sample_list = ['abc', 'xyz', 'aba', '1221']
        self.sort_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        self.duplicated_list = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, ]
        self.word_list = ['a', 'ab', 'asdsafgh', '1221', 'hello', 'world', 'python', 'java', 'javascript', 'c++']
        self.color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        self.char_list = ['P', 'Y', 'T', 'H', 'O', 'N']
        self.shallow_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
        self.list1 = [10, 10, 0, 0, 10]
        self.list2 = [10, 10, 10, 0, 0]
        self.list3 = [1, 10, 10, 0, 0]
        self.sublist1 = [10, 20, 30, 40]
        self.sublist2 = ['X', 'Y', 'Z']
        self.one_to_three = [1, 2, 3]
        self.color1 = "Red", "Green", "Orange", "White"
        self.color2 = "Black", "Green", "White", "Pink"
        self.first_5_numbers = [0, 1, 2, 3, 4, 5]
        self.word_list_1 = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
                     'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']
        self.chars_list1 = ['a', 'b', 'c', 'd', 'e', 'f']
        self.chars_list2 = ['d', 'e', 'f', 'g', 'h']
        self.one_to_fifteen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.pair_of_values = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
        self.nested_colors =  [['Red'], ['Green'], ['Black']]
        self.two_lists = ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
        self.sort_list_sec_value = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
        self.char_list_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
        self.two_color_lists = ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
        self.original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]
        self.color_string = "['Red', 'Green', 'White']"
        self.two_lists_line = [[1, 3, 5, 7, 9, 10], [2, 4, 6, 8]]
        self.random_number_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
        self.list_pairs = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
        self.digital_number_sublist_pair = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        self.words_random_characters = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
        self.list_with_sublist = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
        self.numbers_list2 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]


    # 1. Write a Python program to sum all the items in a list.
    def sum_list(self):
        return sum(self.numbers_list)

    # 2. Write a Python program to multiply all the items in a list.
    def multiply_numbers(self):
        result = 1
        for number in self.numbers_list:
            result *= number
        return result

    # 3. Write a Python program to get the largest number from a list
    def get_largest_number(self):
        return max(self.numbers_list)

    # 4. Write a Python program to get the smallest number from a list.
    def get_smallest_number(self):
        return min(self.numbers_list)

    # 5. Write a Python program to count the number of strings
    # from a given list of strings. The string length is 2 or more
    # and the first and last characters are the same.
    # Sample List : ['abc', 'xyz', 'aba', '1221']
    # Expected Result : 2

    def count_values_of_strings(self):
        count = 0
        for value in self.sample_list:
            if len(value) >= 2 and value[0] == value[-1]:
                count += 1
        return count
    # 6. Write a Python program to get a list, sorted in increasing
    # order by the last element in each tuple from a given list of non-empty tuples.
    # Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    # Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

    def sort_last_element(self):
        return sorted(self.sort_list, key=lambda number: number[1])

    def remove_duplicate(self):
        return list(set(self.duplicated_list))
        result = []
        for number in self.duplicated_list:
            if number not in result:
                result.append(number)
            else:
                continue
        return result

    # 9. Write a Python program to clone or copy a list.
    def clone_list(self):
        new_list = self.numbers_list
        return new_list

    def find_word_by_len(self, length):
        return [word for word in self.word_list if len(word) >= length]

    def has_comment_element(self):
        return any([number for number in self.numbers_list if number in self.numbers_list1])

    # 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
    def remove_index(self, indexes):
        # result = []
        # for index, number in enumerate(self.color_list):
        #     if index not in indexes:
        #         result.append(number)
        # return result
        return [word for index, word in enumerate(self.color_list) if index not in indexes]

    # 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
    def generate_3d_array(self):
        return [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

    # 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
    def remove_odd_numbers(self):
        return [number for number in self.numbers_list if number % 2 == 0]

    def shuffle_list(self):
        shuffle(self.color_list)
        return self.color_list

    def print_square_numbers(self):
        return [number ** 2 for number in range(1, 31)][5:-5]

    def is_prime_number(self, number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def all_prime_numbers(self, numbers):
        return all(self.is_prime_number(num) for num in numbers)

    def difference_between_lists(self):
        # first_difference = list(set(self.numbers_list) - set(self.numbers_list1))
        # second_difference = list(set(self.numbers_list1) - set(self.numbers_list))
        # return first_difference + second_difference
        first_list = [number for number in self.numbers_list if number not in self.numbers_list1]
        second_list = [number for number in self.numbers_list1 if number not in self.numbers_list]
        return first_list + second_list
    # 20. Write a Python program to access the index of a list.

    def find_list_index(self):
        return [(index, color) for index, color in enumerate(self.color_list, start=1)]

    def convert_to_string(self):
        return ''.join(self.char_list)

    def flatten_the_list(self):
        return [element for sublist in self.shallow_list for element in sublist]
#     24. Write a Python program to append a list to the second list.

    def append_to_second_list(self):
        # for number in self.numbers_list:
        #     self.color_list.append(number)
        # return self.color_list
        # return self.numbers_list + self.color_list
        return [item for sublist in [self.numbers_list, self.char_list] for item in sublist]

    # 25. Write a Python program to select an item randomly from a list.
    def select_random_number(self):
        return choice(self.char_list)

    # 26. Write a Python program to check whether two lists are circularly identical.
    def are_circularly_identical(self):
        return ' '.join(map(str, self.list1)) in ' '.join(map(str, self.list2 * 2))

    # 27. Write a Python program to find the second smallest number in a list.
    def find_second_smallest(self):
        unique_numbers = list(set(self.numbers_list))
        if len(unique_numbers) < 2: return None
        else: return sorted(unique_numbers)[1]

    def find_second_largest_number(self):
        unique_numbers = list(set(self.numbers_list))
        if len(unique_numbers) < 2: return None
        else: return sorted(unique_numbers)[-2]

    # 29. Write a Python program to get unique values from a list.
    def get_unique_values(self):
        # return list(set(self.numbers_list))
        unique_list = []
        for number in self.duplicated_list:
            if number not in unique_list:
                unique_list.append(number)
            # else:
            #     unique_list
        return unique_list, self.duplicated_list

    # 30. Write a Python program to get the frequency of elements in a list.
    def count_values(self):
        # return {value: self.duplicated_list.count(value) for value in self.duplicated_list}
        count_dict = {}
        for value in self.duplicated_list:
            if value in count_dict:
                count_dict[value] += 1
            else:
                count_dict[value] = 1
        return count_dict
    # 31. Write a Python program to count the number of elements in a list within a specified range.

    def count_values_in_range(self, range_start, range_end):
        # count_within_range = 0
        # for element in self.duplicated_list:
        #     if range_start <= element <= range_end:
        #         count_within_range += 1
        # return count_within_range
        # count_values = 0
        # values_range = range(range_start, range_end + 1)
        # for value in self.duplicated_list:
        #     if value in values_range:
        #         count_values += 1
        # return count_values
        # return len([element for element in self.duplicated_list if range_start <= element <= range_end])
        return len(list(filter(lambda value: range_start <= value <= range_end, self.duplicated_list)))

    # 32. Write a Python program to check whether a list contains a sublist.
    def check_if_list_contains_sublist(self):
        sublist_length = len(self.duplicated_list)
        return any(
            (self.numbers_list == self.duplicated_list[i:sublist_length + i]) for i in range(len(self.duplicated_list) -
                                                                                             sublist_length + 1))
    # 33. Write a Python program to generate all sublists of a list.
    def generate_all_sublist(self):
        # return [self.sublist1[i: j] for i in range(len(self.sublist1)) for j in range(i + 1, len(self.sublist1) + 1)]
        return [self.sublist2[i: j] for i in range(len(self.sublist2)) for j in range(i + 1, len(self.sublist2) + 1)]

    # 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
    def concat_values(self, n):
        return [f'{char}{value}' for value in range(1, n + 1) for char in ['q', 'p']]

    # 36. Write a Python program to get a variable with an identification number or string.
    def get_variable_id(self, var):
        return id(var)

    # 37. Write a Python program to find common items in two lists.
    def find_comment_items(self):
        # return set(self.color1) & set(self.color2)
        return [value for value in self.color1 if value in self.color2]

    def change_value_position(self):
        for i in range(0, len(self.first_5_numbers), 2):
            if i+1 < len(self.first_5_numbers):
                self.first_5_numbers[i], self.first_5_numbers[i+1] = self.first_5_numbers[i+1], self.first_5_numbers[i]
        return self.first_5_numbers

    def combine_integers_to_one(self):
        # return ''.join([str(number) for number in self.numbers_list])
        return ''.join(map(str, self.numbers_list))

    def take_first_char(self):
        # return [word[0] for word in self.word_list_1]
        # return list(map(lambda word: word[0], self.word_list_1))
        return list(filter(lambda word: word[0], self.word_list_1))

    def create_multiple_lists(self):
        # obj = {}
        # for number in range(1, 21):
        #     obj[str(number)] = []
        # return obj
        return {str(number): [] for number in range(1, 21)}

    # 42. Write a Python program to find missing and additional values in two lists.
    def find_missing_values(self):
        # first_missing_chars = [char for char in self.chars_list1 if char not in self.chars_list2]
        first_missing_chars = list(filter(lambda char: char not in self.chars_list2, self.chars_list1))
        second_missing_chars = [char for char in self.chars_list2 if char not in self.chars_list1]
        return first_missing_chars, second_missing_chars

    def generate_three_lists(self):
        return [[5*i + j for j in range(1, 6)] for i in range(5)]

    # 45. Write a Python program to convert a pair of values into a sorted unique array.
    def convert_pair_values_to_list(self):
        # return set([element for pair in self.pair_of_values for element in pair])
        return sorted(set().union(*self.pair_of_values))

    # 46. Write a Python program to select the odd items from a list.
    def select_odd_item(self):
        # return [number for number in self.one_to_fifteen if number % 2 != 0]
        return list(filter(lambda odd_number: odd_number % 2 != 0, self.one_to_fifteen))

    # 47. Write a Python program to insert an element before each element of a list.
    def insert_element_before(self, element):
        list_with_sublist = [[element, original_element] for original_element in self.numbers_list]
        flat_list = [item for sublist in list_with_sublist for item in sublist]
        return flat_list, list_with_sublist

    def print_nested_list(self):
        # for sublist in self.nested_colors:
        #     for color in sublist:
        #         print(color)
        return '\n'.join([color for sublist in self.nested_colors for color in sublist])

    # 49. Write a Python program to convert a list to a list of dictionaries.
    def convert_list_dictionary(self):
        return [{'color_name': color, 'color code': code} for color, code in zip(self.two_lists[0], self.two_lists[1])]

    # 50. Write a Python program to sort a list of nested dictionaries.
    def sort_list_sec_value_new(self):
        self.sort_list_sec_value.sort(key=lambda element: element['key']['subkey'], reverse=True)
        return self.sort_list_sec_value

    # 51. Write a Python program to split a list every Nth element.
    def split_list_nth_value(self, step):
        return [self.char_list_values[char::step] for char in range(step)]

    def compute_color_list(self):
        # first_sec_list = [color for color in self.two_color_lists[0] if color not in self.two_color_lists[1]]
        first_sec_list = list(filter(lambda color: color not in self.two_lists[1], self.two_color_lists[0]))
        sec_first_list = [color for color in self.two_color_lists[1] if self.two_color_lists not in self.two_color_lists[0]]
        return first_sec_list, sec_first_list

    # 53. Write a Python program to create a list with infinite elements.
    import itertools
    def create_infinite_list(self):
        c = itertools.count()
        print(next(c))
        print(next(c))
        print(next(c))
        print(next(c))

    # 54. Write a Python program to concatenate elements of a list.
    def concat_elements_in_list(self):
        # return ''.join([color.lower() for color in self.color_list])
        return ''.join(map(lambda color:color.lower(), self.color_list))

    # 55. Write a Python program to remove key-value pairs from a list of dictionaries.
    def remove_key_value_pairs(self):
        return [{key: value for key, value in elements.items() if key != 'key1'} for elements in self.original_list]

    # 56. Write a Python program to convert a string to a list.

    import ast

    def convert_string_list(self):
        # return eval(self.color_string)
        return ast.literal_eval(self.color_string)

    # 57. Write a Python program to check if all items in a given list of strings are equal to a given string.

    def check_value_list(self, compare_color):
        return all(color == compare_color for color in self.color_list)

    # 58. Write a Python program to replace the last element in a list with another list.
    def replace_last_element_list(self, new_list):
        self.two_lists_line[0] = self.two_lists_line[0][:-1] + new_list
        return self.two_lists_line[0]

    # 59. Write a Python program to check whether the n-th element exists in a given list.
    def check_element_exist_list(self, index):
        return index < len(self.one_to_fifteen)

    # 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
    def find_second_smallest_value(self):
        return sorted(self.pair_of_values, key=lambda value:value[1])[0]

    # 61. Write a Python program to create a list of empty dictionaries.
    def create_list_empty_dict(self, dict_range):
        return [{} for _ in range(dict_range)]

    # 62. Write a Python program to print a list of space-separated elements.
    def print_values_seperated_space(self):
        return ' '.join([str(number) for number in self.one_to_fifteen])

    # 63. Write a Python program to insert a given string at the beginning of all items in a list.
    def insert_string_beginning(self, my_word):
        # return [my_word + str(number) for number in self.one_to_fifteen]
        return list(map(lambda number: my_word + str(number), self.one_to_fifteen))

    # 64. Write a Python program to iterate over two lists simultaneously.
    def iterate_over_two_lists(self):
        return '\n'.join([str([char, numbers]) for char, numbers in zip(self.one_to_three, self.sublist2 )])

    def add_zeroes_end(self):
        # self.random_number_list.sort()
        # return list(reversed(self.random_number_list))
        # result = []
        # count_zero = sum(1 for number in self.random_number_list if number == 0)
        # remove_zero = [number for number in self.random_number_list if number != 0]
        # for number in remove_zero:
        #     result.append(number)
        # for _ in range(1, count_zero + 1):
        #     result.append(0)
        # return result
        self.random_number_list.sort(key=lambda number: number == 0)
        return self.random_number_list

    # 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
    def find_highest_list(self):
        # return self.list_pairs
        # return min(self.list_pairs, key=sum)
        return max(self.list_pairs, key=sum)

    # 67. Write a Python program to find all the values in a list that are greater than a specified number.
    def find_value_higher_specific_number(self, checking_number):
        return all(number >= checking_number for number in self.numbers_list)

    # 68. Write a Python program to extend a list without appending.
    def extend_list(self):
        sample_data1 = [10, 20, 30]
        sample_data2 = [40, 50, 60]
        sample_data1[:0] = sample_data2
        print(sample_data1)

    def remove_duplicates_sublist(self):
        no_duplicated_list = list(map(list, set(map(tuple, self.digital_number_sublist_pair))))
        no_duplicated_list.sort(key=self.digital_number_sublist_pair.index)
        return no_duplicated_list

    def starts_with_character(self, starting_char):
        # return [word for word in self.words_random_characters if word[0] == starting_char]
        return list(filter(lambda word: word.startswith(starting_char), self.words_random_characters))

    # 71. Write a Python program to check whether all dictionaries in a list are empty or not.
    def check_empty_dictionary(self, testing_values):
        return all([value == {} for value in testing_values])

    def flatten_given_list(self, nested_list):
        if isinstance(nested_list, list):
            return [element for sublist in nested_list for element in self.flatten_given_list(sublist)]
        else:
            return [nested_list]

    # 73. Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.
    def remove_consecutive_numbers(self):
        return [key for key, group in groupby(self.numbers_list2)]


list_solution = ListSolutions()


print(list_solution.remove_consecutive_numbers())
# print(list_solution.flatten_given_list(1))
# print(list_solution.check_empty_dictionary([{},{},{}]))
# print(list_solution.check_empty_dictionary([{1,2},{},{}]))
# print(list_solution.starts_with_character('a'))
# print(list_solution.starts_with_character('d'))
# print(list_solution.remove_duplicates_sublist())
# print(list_solution.extend_list())
# print(list_solution.find_value_higher_specific_number(1))
# print(list_solution.find_highest_list())
# print(list_solution.add_zeroes_end())
# print(list_solution.iterate_over_two_lists())
# print(list_solution.insert_string_beginning('emp'))
# print(list_solution.print_values_seperated_space())
# print(list_solution.create_list_empty_dict(10))
# print(list_solution.find_second_smallest_value())
# print(list_solution.check_element_exist_list(1))
# print(list_solution.replace_last_element_list([2, 4, 6, 8]))
# print(list_solution.check_value_list('red'))
# print(list_solution.check_value_list('White'))
# print(list_solution.check_value_list(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
# print(list_solution.convert_string_list())
# print(list_solution.remove_key_value_pairs())
# print(list_solution.concat_elements_in_list())
# print(list_solution.create_infinite_list())
# print(list_solution.compute_color_list())
# print(list_solution.split_list_nth_value(3))
# print(list_solution.sort_list_sec_value_new())
# print(list_solution.convert_list_dictionary())
# print(list_solution.print_nested_list())
# print(list_solution.insert_element_before('ac'))
# print(list_solution.select_odd_item())
# print(list_solution.convert_pair_values_to_list())
# print(list_solution.generate_three_lists())
# print(list_solution.find_missing_values())
# print(list_solution.create_multiple_lists())
# print(list_solution.take_first_char())
# print(list_solution.combine_integers_to_one())
# print(list_solution.change_value_position())
# print(list_solution.find_comment_items())
# print(list_solution.get_variable_id('hello'))
# print(list_solution.get_variable_id('world'))
# print(list_solution.concat_values(5))
# print(list_solution.generate_all_sublist())
# print(list_solution.check_if_list_contains_sublist())
# print(list_solution.count_values_in_range(1, 3))
# print(list_solution.count_values())
# print(list_solution.get_unique_values())
# print(list_solution.find_second_largest_number())
# print(list_solution.find_second_smallest())
# print(list_solution.are_circularly_identical())
# print(list_solution.select_random_number())
# print(list_solution.append_to_second_list())
# print(list_solution.flatten_the_list())
# print(list_solution.convert_to_string())
# print(list_solution.find_list_index())
# print(list_solution.difference_between_lists())
# print(list_solution.is_prime_number(5))
# print(list_solution.all_prime_numbers([0, 3, 4, 7, 9]))
# print(list_solution.all_prime_numbers([3, 5, 7, 13]))
# print(list_solution.print_square_numbers())
# print(list_solution.shuffle_list())
# print(list_solution.remove_odd_numbers())
# print(list_solution.generate_3d_array())
# print(list_solution.remove_index([0, 4, 5]))
# print(list_solution.has_comment_element())
# print(list_solution.find_word_by_len(10))
# print(list_solution.find_word_by_len(4))
# print(list_solution.clone_list())
# print(list_solution.remove_duplicate())
# # print(list_solution.sort_last_element())
# print(list_solution.count_values_of_strings())
# print(list_solution.get_smallest_number())
# print(list_solution.get_largest_number())
# print(list_solution.sum_list())
# print(list_solution.multiply_numbers())
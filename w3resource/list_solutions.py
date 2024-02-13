# 1. Write a Python program to sum all the items in a list.
from random import shuffle, choice


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


list_solution = ListSolutions()

print(list_solution.generate_all_sublist())
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
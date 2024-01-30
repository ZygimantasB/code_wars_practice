# 1. Write a Python program to sum all the items in a list.

class ListSolutions:

    def __init__(self):
        self.numbers_list = [1, 2, 3, 33, 4, 9, 10, 10]
        self.numbers_list1 = [1, 12, 13, 14, 15, 16, 17]
        self.sample_list = ['abc', 'xyz', 'aba', '1221']
        self.sort_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        self.duplicated_list = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, ]
        self.word_list = ['a', 'ab', 'asdsafgh', '1221', 'hello', 'world', 'python', 'java', 'javascript', 'c++']
        self.color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

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


list_solution = ListSolutions()

print(list_solution.remove_index([0, 4, 5]))
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
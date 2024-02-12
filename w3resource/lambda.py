from datetime import datetime
from functools import reduce


class LambdaSolutions:

    def __init__(self):
        self.tuple_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        self.dictionary_values = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7,
                                                                                  'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
        self.numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.sentence = 'My name is Friday'
        self.date_time = datetime(2020, 1, 15, 9, 3, 32)
        self.string_number_list = ['a', 1, 'hello', 2, 'world', 3, 'python', 4, 'is', 5, 'awesome']
        self.numbers1 = [1, 2, 3, 5, 7, 8, 9, 10]
        self.numbers2 = [1, 2, 4, 8, 9]
        self.positive_negative = [-1, 2, -3, 5, 7, 8, 9, -10]
        self.grades = [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
        self.divisible_number = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
        self.words_example = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
        self.words_for_anagram = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
        self.find_numbers_sample = '23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
        self.sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
        self.negative_positive_numbers = [2, 4, -6, -9, 11, -12, 14, -5, 17]


    def add_numbers(self, number):
        return (lambda x: x + 15)(number)

    def multiply_number(self, number1, number2):
        return (lambda x, y: x * y)(number1, number2)

    def operations_numbers(self, number1):
        double_number = (lambda number:  number * 2)(number1)
        triple_number = (lambda number: number * 3)(number1)
        quadruple_number = (lambda number: number * 4)(number1)
        quintuple_number = (lambda number: number * 5)(number1)
        return double_number, triple_number, quintuple_number, quadruple_number

    def sort_given_list(self):
        return sorted(self.tuple_list, key=lambda number: number[1])

    def sort_given_dict(self):
        return sorted(self.dictionary_values, key=lambda value: str(value['model']))

    def filter_even_odd(self):
        odd_numbers = list(filter(lambda number: number % 2 != 0, self.numbers_list))
        even_numbers = list(filter(lambda number: number % 2 == 0, self.numbers_list))
        return odd_numbers, even_numbers

    def check_length(self):
        return list(filter(lambda day: len(day) == 6, self.weekdays))

    def make_square_list(self):
        return list(map(lambda number: number ** 2, self.numbers_list))

    def make_cube_list(self):
        return list(map(lambda number: number ** 3, self.numbers_list))

    def check_starting_work(self):
        return any(list(map(lambda word: word.startswith('My'), self.sentence.split())))

    def extract_date_time(self):
        # return {
        #     'year': self.date_time.year,
        #     'month': self.date_time.month,
        #     'day': self.date_time.day,
        #     'time': self.date_time.time(),
        # }
        get_year = (lambda date: date.year)(self.date_time)
        get_month = (lambda date: date.month)(self.date_time)
        get_day = (lambda date: date.day)(self.date_time)
        get_time = (lambda date: date.time())(self.date_time)

        return {
            'year': get_year,
            'month': get_month,
            'day': get_day,
            'time': get_time
        }

    def is_number(self):
        return list(map(lambda number: str(number).isdigit(), self.string_number_list))

    def create_fibonacci(self, n):
        fibonacci_series = reduce(lambda x, _: x.append(sum(x[-2:])) or x, range(2, n), [0, 1])
        return fibonacci_series

    def find_intersection(self):
        return list(filter(lambda number: number in self.numbers1, self.numbers2))

    def regenerate_list(self):
        # positive_number = list(filter(lambda number: number >= 0, self.positive_negative))
        # negative_number = list(filter(lambda number: number <= 0, self.positive_negative))
        # return positive_number + negative_number
        return sorted(self.positive_negative, key=lambda number: (number < 0, number))

    def count_even_odd_number(self):
        even_numbers =  len(list(filter(lambda number: number % 2 == 0, self.numbers1)))
        odd_numbers = len(list(filter(lambda number: number % 2 != 0, self.numbers1)))
        return f'Even: {even_numbers} Odd: {odd_numbers}'

    def filter_weekdays(self):
        return list(filter(lambda day: len(day) == 6, self.weekdays))

    def add_two_lists(self):
        return list(map(lambda number1, number2: number1 + number2, self.numbers1, self.numbers2))

    def find_second_grade(self):
        return sorted(self.grades, key=lambda grade: grade[1])

    def find_divisible_numbers(self):
        return list(filter(lambda number: number % 19 == 0 or number % 13 == 0, self.divisible_number))

    def find_palindrome(self):
        return list(filter(lambda word: word == word[::-1], self.words_example))

    def make_anagram(self, this_word):
        return list(filter(lambda word: sorted(word) == sorted(this_word), self.words_for_anagram))

    def find_numbers(self):
        words = self.find_numbers_sample.split()
        numbers = list(map(int, filter(lambda word: word.isdigit(), words)))
        filtered_numbers = list(filter(lambda number: len(str(number)) > len(numbers), numbers))
        sorted_numbers = sorted(filtered_numbers)
        return sorted_numbers

    # 21 exercise.
    def multiply_list(self, multiply_number):
        return list(map(lambda number: number ** multiply_number, self.numbers1))

    def sum_sample_names(self):
        # no_upper_case = list(filter(lambda name: name[0].islower() and name[1:].islower(), self.sample_names))
        # return len(''.join(no_upper_case))
        filtered_names = filter(lambda name: name[0].isupper(), self.sample_names)
        lengths = map(len, filtered_names)
        return sum(lengths)

    def add_negative_positive_numbers(self):
        negative_numbers = sum(list(filter(lambda number: number < 0, self.negative_positive_numbers)))
        positive_numbers = sum(list(filter(lambda number: number > 0, self.negative_positive_numbers)))
        return f'Negative: {negative_numbers}, Positive: {positive_numbers}'

    def find_divisible_numbers_new(self, start, end):
        return [
            number for number in range(start, end + 1)
            if all(map(lambda x: int(x) != 0 and number % int(x) == 0, str(number)))
        ]
    # 25. Write a Python program to create the next bigger number by rearranging the digits of a given number.


lambda_solutions = LambdaSolutions()
print(lambda_solutions.find_divisible_numbers_new(1, 12))
# print(lambda_solutions.add_negative_positive_numbers())
# print(lambda_solutions.sum_sample_names())
# print(lambda_solutions.multiply_list(2))
# print(lambda_solutions.find_numbers())
# print(lambda_solutions.find_numbers())
# print(lambda_solutions.make_anagram('abcd'))
# print(lambda_solutions.make_anagram('bcda'))
# print(lambda_solutions.make_anagram('cbea'))

# print(lambda_solutions.find_palindrome())
# print(lambda_solutions.find_divisible_numbers())
# print(lambda_solutions.find_second_grade())
# print(lambda_solutions.add_two_lists())
# print(lambda_solutions.filter_weekdays())
# print(lambda_solutions.count_even_odd_number())
# print(lambda_solutions.regenerate_list())
# print(lambda_solutions.find_intersection())
# print(lambda_solutions.create_fibonacci(2))
# print(lambda_solutions.is_number())
# print(lambda_solutions.extract_date_time())
# print(lambda_solutions.add_numbers(10))
# print(lambda_solutions.multiply_number(5, 15))
# print(lambda_solutions.operations_numbers(15))
# print(lambda_solutions.sort_given_list())
# print(lambda_solutions.sort_given_dict())
# print(lambda_solutions.filter_even_odd())
# print(lambda_solutions.check_length())
# print(lambda_solutions.make_square_list())
# print(lambda_solutions.make_cube_list())
# print(lambda_solutions.check_starting_work())
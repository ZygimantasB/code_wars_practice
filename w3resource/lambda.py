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


lambda_solutions = LambdaSolutions()
print(lambda_solutions.find_intersection())
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
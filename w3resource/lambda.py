class LambdaSolutions:

    def __init__(self):
        self.tuple_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        self.dictionary_values = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7,
                                                                                  'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
        self.numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


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

lambda_solutions = LambdaSolutions()
# print(lambda_solutions.add_numbers(10))
# print(lambda_solutions.multiply_number(5, 15))
# print(lambda_solutions.operations_numbers(15))
# print(lambda_solutions.sort_given_list())
# print(lambda_solutions.sort_given_dict())
print(lambda_solutions.filter_even_odd())

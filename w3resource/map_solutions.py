class MapSolutions:

    def __init__(self):
        self.numbers_tuple = (1, 2, 3, 4, 5, 6, 7)

    def triple_number(self):
        return list(map(lambda number: number + number + number, self.numbers_tuple))

    # 2. Write a Python program to add three given lists using Python map and lambda.
    def add_three_lists(self):
        pass



map_solutions = MapSolutions()
print(map_solutions.triple_number())

# https://www.w3resource.com/python-exercises/python-basic-exercise-6.php

from math import pi
from typing import List
from sys import version
from datetime import datetime

class PythonBasicPart1:

    def __init__(self) -> None:
        self.task_1_sentence = "Twinkle, twinkle, little star,\n\t How I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky.\n\t Twinkle, twinkle, little star, How I wonder what you are"

    def task_1(self) -> str:
        return self.task_1_sentence

    def task_2(self) -> str:
        return version

    def task_3(self) -> datetime:
        return datetime.now()

    def task_4(self, r: float) -> float:
        return pi * r**2

    def task_5(self) -> str:
        name = input('Write your name: ')
        # return ''.join(reversed(name))
        return name[::-1]

    def task_6(self) -> str:
        numbers = input('Write your numbers: ')
        list_numbers = list(numbers.split(','))
        tuple_numbers = tuple(numbers.split(','))
        return f'Type {type(list_numbers)} Numbers: {list_numbers}\nType {type(tuple_numbers)} Tuples: {tuple_numbers}'


basic = PythonBasicPart1()
print(basic.task_6())

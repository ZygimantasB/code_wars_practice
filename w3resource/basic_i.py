# https://www.w3resource.com/python-exercises/python-basic-exercise-6.php

import calendar

from math import pi
from typing import List
from sys import version
from datetime import datetime, date


class PythonBasicPart1:

    def __init__(self) -> None:
        self.task_1_sentence = "Twinkle, twinkle, little star,\n\t How I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky.\n\t Twinkle, twinkle, little star, How I wonder what you are"
        self.color_list = ["Red","Green","White" ,"Black"]

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

    def task_7(self) -> str:
        file_name = input('Write a file name: ')
        extension = file_name.split('.')
        return f'Extension is: {extension[-1]}'

    def task_8(self) -> str:
        # first_color = self.color_list[0]
        # last_color = self.color_list[-1]
        # return first_color + ' ' + last_color

        first, *_, last = self.color_list
        return f'{first} {last}'

    def task_9(self) -> str:
        exam_st_date = (11, 12, 2014)
        date_str = ' / '.join(map(str, exam_st_date))
        return date_str

    def task_10(self, number) -> int:
        # return number + int(str(number)*2) + int(str(number)*3)
        return sum(int(str(number) * i) for i in range(1, 4))

    def task_11(self, function_name=None) -> str:
        if function_name is None:
            function_name = abs
        return function_name.__doc__

    def task_12(self, month: int = None, year: int = None) -> str:
        if month is None:
            month = int(input('Write your month: '))
            if year is None:
                year = int(input('Write your year: '))
        return calendar.month(year, month)

    def task_13(self) -> str:
        heredoc = """a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example"""
        return heredoc

    def task_14(self, first_date: tuple, second_date: tuple) -> str:
        date1 = date(*first_date)
        date2 = date(*second_date)
        delta = date2 - date1
        return f"{delta.days} days ago"

    def task_15(self, r: float = 6) -> float:
        return (4/3) * pi * r**3

    def task_16(self, number) -> float:
        # if number > 17:
        #     return (number - 17) * 2
        # else:
        #     return 17 - number
        diff = number - 17
        return diff * 2 if diff > 0 else (abs(diff))

    def task_17(self, number: int) -> bool:
        return abs(number - 1000) <= 100 or abs(number - 2000) <= 100



basic = PythonBasicPart1()
print(basic.task_17(1800))

import sys
import datetime

from math import pi

class PythonBasicPart1:

    def __init__(self):
        self.task_1_sentence = "Twinkle, twinkle, little star,\n\t How I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky.\n\t Twinkle, twinkle, little star, How I wonder what you are"

    def task_1(self):
        return self.task_1_sentence

    def task_2(self):
        return sys.version

    def task_3(self):
        return datetime.datetime.now()





basic = PythonBasicPart1()
print(basic.task_3())


# import re
#
#
# def validate_usr(username):
#     return re.match(r'^[a-z0-9_]{4,16}$', username) is not None

# def number_to_string(num):
#     return str(num)


# def pluck(objs, name):
#     return [obj.get(name, None) for obj in objs]

def digitize(numbers):
    return [int(number)for number in str(numbers)[::-1]]


# print(digitize(35231))

def square(number):
    return number * number


numbers = [1, 2, 3, 4, 5]

result = list(map(square, numbers))
# print(result)


def _all(seq, fun):
    return all(fun(i) for i in seq)


def get_drink_by_profession(param):
    profession_to_drink = {
        'Jabroni': "Patron Tequila",
        "School Counselor": 	"Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": 	"Your tax dollars",
        "Rapper": 	"Cristal",
    }

    return profession_to_drink.get(param.title(), 'Beer')


# print(get_drink_by_profession('Jabroni'))
# print(get_drink_by_profession('School Counselor'))
# print(get_drink_by_profession('Programmer'))

def sum_array(arr):
    # if arr is None or len(arr) == 0 or len(arr) == 1:
    #     return 0
    # sorted_list = sorted(arr)
    # return sum(sorted_list[1:-1])
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0


# print(sum_array([6, 2, 1, 8, 10]))
# print(sum_array([6, 2, 1, 8, 10]))
# print(sum_array([None]))


def repeat_str(repeat, string):
    return string * repeat


# print(repeat_str(6, 'I'))
# print(repeat_str(6, 'Hello'))


def make_negative(number):
    # return -number if number > 0 else number
    return -abs(number)

# print(make_negative(-1))
# print(make_negative(1))
# print(make_negative(-8))
# print(make_negative(8))


def rps(p1, p2):
    # if p1 == p2:
    #     return 'Draw!'
    # elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') \
    #     or (p1 == 'paper' and p2 == 'rock'):
    #     return 'Player 1 won!'
    # else:
    #     return 'Player 2 won!'
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return 'Plater 1 wins!'
    elif beats[p2] == p1:
        return 'Player 2 wins'
    else:
        return 'Draw'


# print(rps('paper', 'paper'))
# print(rps('paper', 'scissors'))
# print(rps('paper', 'rock'))


from math import log


def logs(x, a, b):
    return log(a, x) + log(b, x)


# print(logs(10, 2 ,3))

from math import floor

def get_average(marks):
    return floor(sum(marks) / len(marks))


# print(get_average([2, 2, 2, 2]))


def remove_every_other(my_list):
    return my_list[::2]


# print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))

class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self,n):
        if self.lives <= 0: raise Exception('No lives left')
        elif self.number == n: return True
        self.lives -= 1
        return False


# guesser = Guesser(5, 3)
# print(guesser.guess(3))
# print(guesser.guess(3))
# print(guesser.guess(3))
# print(guesser.guess(5))


def converter(mpg):
    return round(mpg * 0.354006, 2)


# print(converter(10))

def solution(string):
    return string[::-1]


# print(solution('world'))

def positive_sum(arr):
    return sum([number for number in arr if number > 0])


# print(positive_sum([1,-4,7,12]))


def basic_op(operator, value1, value2):
    match operator:
        case '+':
            return value1 + value2
        case '-':
            return value1 - value2
        case '*':
            return value1 * value2
        case '/':
            return value1 / value2

# def basic_op(operator, value1, value2):
#     ops = {'+': lambda a, b: a + b,
#            '-': lambda a, b: a - b,
#            '*': lambda a, b: a * b,
#            '/': lambda a, b: a / b}
#     return ops[operator](value1, value2)

# print(basic_op('+', 4, 7))
# print(basic_op('-', 4, 7))
# print(basic_op('*', 4, 7))
# print(basic_op('/', 4, 7))


def sum_array(a):
    return sum(a)


# print(sum_array([1, 5.2, 4, 0, -1]))

def how_much_i_love_you(nb_petals):
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    # The index for the phrase is (petals - 1) % 6, as the list index starts from 0
    return phrases[(nb_petals - 1) % 6]


# print(how_much_i_love_you())

def corrections(x):
    if x > 0:
        return str(x) + " is more than zero."
    else:
        return str(x) + " is equal to or less than zero."


import sys
def total_bytes(obj):
    return sys.getsizeof(obj)


# print(total_bytes('hello'))

def pillars(num_pill, dist, width):
    if num_pill <= 0:
        return False
    else:
        distance_between_cm = dist * 100
        total_distance = (num_pill - 1) * distance_between_cm
        total_distance -= width * (num_pill - 2)
        return total_distance


def sakura_fall(v: int) -> int:
    if v <= 0:
        return 0

    height = 5 * 80

    return height / v


def multi_table(number):
    result = []
    for i in range(1, 11):
        result.append(f'{i} * {number} = {i * number}')
    return '\n'.join(result)

print(multi_table(5))

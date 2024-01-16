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

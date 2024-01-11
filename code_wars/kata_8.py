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
print(result)

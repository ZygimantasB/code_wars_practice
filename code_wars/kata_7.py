def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 = p0 + p0 * (percent / 100) + aug
        p0 = int(p0)
        years + + 1
    return years


# print(nb_year(1500, 2, 000, 5000), 15)
# print((nb_year(1500000, 2.5, 10000, 2000000), 10))


# def num_of_open_lockers(lockers):
#     count = 1000
#     for locker in range(1, lockers + 1):
#         if locker % 2 == 0:
#             count -= 1
#         if locker % 3 == 0:
#             count += 1
#         if locker % 4 == 0:
#             count += 1
#     return count

def num_of_open_lockers(n):
    square_root = 0
    while (square_root + 1) ** 2 <= n:
        square_root += 1
    return square_root


# print(num_of_open_lockers(1000))

from string import punctuation, digits


def is_it_a_num(s: str) -> str:
    digits = ''.join(filter(str.isdigit, s))

    if len(digits) == 11 and digits.startswith('0'):
        return digits
    else:
        return "Not a phone number"


# Example usage
input_example = "efRFS:)0207ERGQREG88349F82!"


# print(is_it_a_num(input_example))


def range_bit_count(a: int, b: int) -> int:
    # binary_numbers = ''.join([bin(number)[2:] for number in range(a, b + 1)])
    # return sum([1 for number in binary_numbers if number == '1'])
    # count = 0
    # for number in range(a, b + 1):
    #     binary_representation = bin(number)[2:]
    #     count += binary_representation.count('1')
    # return count
    return sum(bin(number).count('1') for number in range(a, b + 1))


# print(range_bit_count(2, 7))


def to_jaden_case(string):
    # return string.title()
    # return ' '.join([word.upper()[0] + word[1:] for word in string.split()])
    return ' '.join(word.capitalize() for word in string.split())


# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

def friend(x):
    return [name for name in x if len(name) == 4]


# print(friend(["Ryan", "Kieran", "Jason", "Yous"],))
# print(friend(['Ryan', 'abc', 'd']))

def number(bus_stops):
    total_people = 0

    for on, off in bus_stops:
        total_people += on - off
    total_people = max(total_people, 0)

    return total_people


bus_stops = [(10, 0), (3, 5), (2, 5)]
# print(number(bus_stops))


def max_multiple(divisor, bound):
    result = []
    for number in range(0, bound + 1):
        if number % divisor == 0 and bound >= number > 0:
            result.append(number)
    return max(result)
    # return bound - (bound % divisor)


# print(max_multiple(2, 7))
# print(max_multiple(10, 50))
# print(max_multiple(7, 100))


def multiple(number):
    if number % 3 == 0 and number % 5 == 0:
        return "BangBoom"
    elif number % 3 == 0:
        return "Bang"
    elif number % 5 == 0:
        return "Boom"
    else:
        return "Miss"
# def multiple(x):
#     if x % 15 == 0: return "BangBoom"
#     if x % 5 == 0: return "Boom"
#     if x % 3 == 0: return "Bang"
#     return "Miss"


# print(multiple(30))
# print(multiple(3))
# print(multiple(98))
# print(multiple(65))
# print(multiple(23))
# print(multiple(15))

def filter_list(sample_list):
    return [number for number in sample_list if isinstance(number, int)]
    # return [x for x in l if type(x) is not str]


# print(filter_list([1,2,'a','b']))


def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


# print(is_anagram('cinema', 'iceman'))
# print(is_anagram('cinema', 'icema'))

def accum(st):
    # result = []
    # for index, char in enumerate(st):
    #     transformed_char = char.upper() + char.lower() * index
    #     result.append(transformed_char)
    # return '-'.join(result)
    return '-'.join([char.upper() + char.lower() * index for index, char in enumerate(st)])


# print(accum('abcd'))
# print(accum('RqaEzty'))
# print(accum('cwAt'))

def get_the_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    expected_vowel_index = 0

    for char in word:
        if char == vowels[expected_vowel_index]:
            count += 1
            expected_vowel_index = (expected_vowel_index + 1) % len(vowels)
        elif char == 'a' and expected_vowel_index != 0:
            # Continue without resetting if 'a' is not the start of the sequence
            continue
        # No reset of count or expected_vowel_index for other non-consecutive vowels

    return count


# print(get_the_vowels('agrtertyfikfmroyrntbvsukldkfa'))
# print(get_the_vowels('erfaiekjudhyfimngukduo'))

def shorter_reverse_longer(a, b):
    # if len(a) > len(b) or len(a) == len(b):
    #     return b + a[::-1] + b
    # else:
    #     return a + b[::-1] + a
    return b + a[::-1] + b if len(a) > len(b) or len(a) == len(b) else a + b[::-1] + a


# print(shorter_reverse_longer('first', 'abcde'))
# print(shorter_reverse_longer('hello', 'bau'))
# print(shorter_reverse_longer('abcde', 'fghi'))
# print(shorter_reverse_longer('pbwmcskx', 'qvkwwmoaai'))

def square_digits(num):
    return int(''.join(str(int(digit)**2) for digit in str(num)))


# print(square_digits(9119))

def close_to_zero(t):
    if not t:
        return 0
    temperatures = list(map(int, t.split()))
    temperatures.sort(key=lambda x: (abs(x), -x))
    return temperatures[0]


# print(close_to_zero('-1 50 -4 20 22 -7 0 10 -8'))


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(is_leap_year(2020))
print(is_leap_year(2000))
print(is_leap_year(2015))
print(is_leap_year(2100))
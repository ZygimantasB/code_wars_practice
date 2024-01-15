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


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

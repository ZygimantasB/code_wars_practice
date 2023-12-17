def calculate_multiplication():
    while True:
        first_number = int(input('First number: '))
        second_number = int(input('Second number: '))
        print(first_number * second_number)
        repeat = input('Do you want to repeat: ').lower()
        if repeat == 'no':
            break


# calculate_multiplication()

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”


def print_name_asterix():
    print('Name', 'Is', 'James', sep='**')


# print_name_asterix()

# Exercise 3: Convert Decimal number to octal using print() output formatting


def convert_decimal_to_octa(decimal_number):
    return oct(decimal_number)[2:]


# print(convert_decimal_to_octa(10))
# print(convert_decimal_to_octa(8))


# Exercise 4: Display float number with 2 decimal places using print()

def display_float_number(float_num):
    # return f'{float_num:.2f}'
    return round(float_num, 2)


num = 458.541315

# print(display_float_number(num))

# Exercise 5: Accept a list of 5 float numbers as an input from the user


def add_float_number(list_size):
    float_list = []
    while len(float_list) != list_size:
        number = float(input('Float number: '))
        float_list.append(number)
    return float_list


# print(add_float_number(5))


# Exercise 6: Write all content of a given file into a new file by skipping line number 5

def read_file_information(file_name):
    with open(file_name, 'r') as file:
        lines = [line.strip() for index, line in enumerate(file.readlines()) if index != 5]
        for line in lines:
            print(line)


file_path = 'G:\Python GitHub ZygimantasB\code_wars_practice\pynative\ test.txt'


# read_file_information(file_path)

# Exercise 7: Accept any three string from one input() call

# strings = input('Enter three strings: ').split()
# for i, string in enumerate(strings, 1):
#     # print(f'Name{i}', string)


# Exercise 7: Accept any three string from one input() call

#
# name_input = input('Enter three strings: ')
# for index, name in enumerate(name_input.split(), 1):
#     print(f'Name{index}: {name}')

# Exercise 8: Format variables using a string.format() method.

totalMoney = 1000
quantity = 3
price = 450


def enter_information(user_money, user_quantity, user_price):
    return f'I have {user_money} dollars so I can but {user_quantity} football for {user_price:.2f} dollars'


# print(enter_information(totalMoney, quantity, price))

# Exercise 10: Read line number 4 from the following file


def add_lines_to_txt_files(name):
    with open('test1.txt', 'a') as file:
        for value in range(1, 8):
            file.write(f'name{name}{value}\n')


# add_lines_to_txt_files('line')

def read_file_information(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())


read_file_information(r'G:\Python GitHub ZygimantasB\code_wars_practice\pynative\test1.txt')

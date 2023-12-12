def calculate_multiplication():
    while True:
        first_number = int(input('First number: '))
        second_number = int(input('Second number: '))
        print(first_number * second_number)
        repeat = input('Do you want to repeat: ').lower()
        if repeat == 'no':
            break


calculate_multiplication()

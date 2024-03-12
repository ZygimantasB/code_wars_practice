from itertools import groupby

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
grouped_numbers = groupby(numbers, key=lambda number: number % 2 == 0)

for key, group in grouped_numbers:
    print('Even' if key else 'Odd', list(group))

words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
grouped_sorted = groupby(words, key=lambda word: word[0])

for key, group in grouped_sorted:
    print(key, list(group))


data = [
    {'name': 'John', 'age': 15},
    {'name': 'Jane', 'age': 15},
    {'name': 'Dave', 'age': 12},
    {'name': 'Jessica', 'age': 12},
    {'name': 'Bill', 'age': 17},
]

grouped_dats = groupby(data, key=lambda value: value['age'])
for key, group in grouped_dats:
    print(key, list(group))

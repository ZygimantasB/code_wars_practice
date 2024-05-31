# https://www.youtube.com/watch?v=K8L6KVGG-7o

import re

text_to_search = r'''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\d') # \d is a digit (0-9)
# pattern = re.compile(r'\D') # \D is not a digit
# pattern = re.compile(r'\w') # \w is a word character (a-z, A-Z, 0-9, _)
# pattern = re.compile(r'\W') # \W is not a word character
# pattern = re.compile(r'\s') # \s is whitespace (space, tab, newline)
pattern = re.compile(r'\S') # \S is not whitespace
# pattern = re.compile(r'\S')


matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[1:4])


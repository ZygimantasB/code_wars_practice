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
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

'''

emails = '''
CoreyMSchafer@gmaiI.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''


sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\d') # \d is a digit (0-9)
# pattern = re.compile(r'\D') # \D is not a digit
# pattern = re.compile(r'\w') # \w is a word character (a-z, A-Z, 0-9, _)
# pattern = re.compile(r'\W') # \W is not a word character
# pattern = re.compile(r'\s') # \s is whitespace (space, tab, newline)
# pattern = re.compile(r'\S') # \S is not whitespace
# pattern = re.compile(r'\bHa') # \b is word boundary
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
# pattern = re.compile(r'[89][0-9]{2}[-.]\d{3}[-.]\d{4}')
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
pattern = re.compile(r'start', re.IGNORECASE)


matches = pattern.findall(sentence)

# findall returns a list of all matches
# match returns the first match

# print(matches)

for match in matches:
    print(match)

# with open('data.txt', 'r', encoding='utf-8') as file:
#     contents = file.read()
#
#     matches = pattern.finditer(contents)
#
#     for match in matches:
#         print(match)

# print(text_to_search[1:4])

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w*)(\.\w*)')

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

matches = pattern.finditer(urls)

for match in matches:
    print(match.group(3)) # group 0 is the entire match

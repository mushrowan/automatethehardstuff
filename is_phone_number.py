#!/usr/bin/python3


def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range (8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?')
print(is_phone_number('415-555-4242'))
print('Is "Killbastard" a phone number?')
print(is_phone_number('Killbastard'))


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print('Phone number found: ' + chunk)
print('Done')


import re

phone_number_regex = re.compile(r'\d{3}-\d{3}-\d{4}')

mo = phone_number_regex.search(message) # This only matches one item. We should make it match multiple items so that we can repurpose it to make the previous task easier.
print('Phone number found: ' + mo.group())


#!/usr/bin/python3

import pyperclip, re

'''
1. Get all the text off the clipboard.
2. Find all the phone numbers and email addresses in the text.
3. Paste them onto the clipboard.


'''

input_string = str(pyperclip.paste())

email_regex = re.compile(r'''(

    (\w+(\.\w+)*)       # Captures ghjk, fsdfa.adsfad, but not .asdfads., asdf..adfdsaf
    (@)                 # Obvious @ is obvious
    (\w+(\.\w+)+)       # Captures asd.adsf but not asdfad

)''', re.VERBOSE)

# TODO: Create a phone number regex
phone_number_regex = re.compile(r'''(

    (0|\+440?|\+3530?)  # Capture the country code (probably there is an easier way to do this but we'll figure it out later)
    (\d{9,10})          # Capture the rest of the number. For British numbers there are 9 or 10 digits to follow

)''', re.VERBOSE)

# TODO: Put text into the clipboard

output_list = phone_number_regex.findall(input_string) + email_regex.findall(input_string)
output_string = ''
for match in output_list:
    output_string += match[0]
    output_string += '\n'




pyperclip.copy(str(output_string))


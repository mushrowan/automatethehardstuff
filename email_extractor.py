#!/usr/bin/python3

import pyperclip, re

'''
1. Get all the text off the clipboard.
2. Find all the phone numbers and email addresses in the text.
3. Paste them onto the clipboard.


'''

# TODO: Get text from the clipboard
input_string = str(pyperclip.paste())
# TODO: Create an email address regex
email_regex = re.compile(r'''(
(\w+(\.\w+)*)       # Captures ghjk, fsdfa.adsfad, but not .asdfads., asdf..adfdsaf
(@)                 # Obvious @ is obvious
(\w+(\.\w+)+)       # Captures asd.adsf but not asdfad
)
''', re.VERBOSE)
# TODO: Create a phone number regex

# TODO: Put text into the clipboard


#!/usr/bin/env python3
"""
Exercise  11.1: Write a simple program to simulate the operation of the grep
command on Unix. Ask the user to enter a regular expression and count the
number of lines that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
import re

def countLine():
    
    count = 0                               # Initialize variables

    text = input('Enter file name: ').lower()
    input_exp = input('Enter a regular expression: ')
    reg_exp = str(input_exp)                # Regular Expressions are strings
    fhand = open(text)

    for line in fhand:
        line = line.rstrip()

    # Only counts if something was found
        if re.findall(reg_exp, line) != []:
            count += 1

    
    print(text + ' had ' + str(count) + ' lines that matched ' + reg_exp)

countLine()
while True:
    ask = input('Wanna count? (y/n) ')
    if ask == 'y' or ask == 'Y':
        countLine()
    else:
        quit()

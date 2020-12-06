"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
# Filter calls with only incoming calls from Bangalore prefix (080)

def extract_area_code(number: str):
    if number.startswith('('):  # area code
        end_index = number.find(')')
        return number[:end_index+1]
    elif number.startswith(('7', '8', '9')):  # mobile number
        return number[:4]
    return None


def bangalore_prefix(number: str):
    prefix = '(080)'
    if (number.startswith(prefix)):
        return True
    return False


def find_all_bangalore_numbers(calls):

    bangalore_list = []  # Space: O(n)
    for call in calls:  # O(n)
        if bangalore_prefix(call[0]):
            bangalore_list.append(call)

    return bangalore_list


def part_a(calls):

    prefix_list = []
    bangalore_numbers = find_all_bangalore_numbers(calls)
    for call in bangalore_numbers: # Time: O(n) 
        n = extract_area_code(call[1])
        if not n in prefix_list:
            prefix_list.append(n)

    prefix_list = sorted(prefix_list)

    message = "The numbers called by people in Bangalore have codes:\n"
    for n in prefix_list:
        message += '{}\n'.format(n)
    print(message)

    return prefix_list

def part_b(calls):

    ratio = 0.0
    bangalore_numbers = find_all_bangalore_numbers(calls)
    bangalore_calls_only = 0
    for call in bangalore_numbers:
        if bangalore_prefix(call[1]):
            bangalore_calls_only += 1

    ratio = bangalore_calls_only / len(bangalore_numbers) * 100

    print ("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(ratio))

# Tests
# assert len(find_all_bangalore_numbers(calls)) > 0
# assert bangalore_prefix('(080)45291968') == True
# assert bangalore_prefix('98446 66723') == False
# assert extract_area_code('(04344)316423') == '(04344)'
# assert extract_area_code('98446 66723') == '9844'
# assert extract_area_code('48446 66723') == None
# print('Tests finished.')

part_a(calls)
part_b(calls)

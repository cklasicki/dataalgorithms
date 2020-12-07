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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def task4(calls, texts):

    telemarketers = set()
    all_outgoing_numbers = set()

    for item in calls:
        all_outgoing_numbers.add(item[1])

    for item in texts:
        all_outgoing_numbers.add(item[0])
        all_outgoing_numbers.add(item[1])

    for number in calls:
        if not number[0] in all_outgoing_numbers:
            telemarketers.add(number[0])

    telemarketers = sorted(telemarketers)

    print("These numbers could be telemarketers: ")
    for n in telemarketers:
        print('{}'.format(n))


task4(calls, texts)

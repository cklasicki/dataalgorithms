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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def add_numbers_from_set(list, unique_numbers_list):

    for item in list: #O(n)
        incoming, answering, *data = item
        unique_numbers_list.add(incoming) #O(1)
        unique_numbers_list.add(answering) #O(1)

# Time O(n), Space O(n)
def unique_numbers(calls, texts):

    unique_numbers_list = set()

    add_numbers_from_set(calls, unique_numbers_list)
    add_numbers_from_set(texts, unique_numbers_list)

    print("There are {} different telephone numbers in the records.".format(
        len(unique_numbers_list)))


unique_numbers(calls, texts)

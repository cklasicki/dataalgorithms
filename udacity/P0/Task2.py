"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def add_number_duration(number, duration, list):
    if number in list:
        list[number] += duration
    else:
        list[number] = duration

def get_the_longest_number_duration(numbers_list):

    number = max(numbers_list, key = lambda k: numbers_list[k])
    return number, numbers_list[number] 

def longest_call(calls):

    numbers_list = {} #holds information about msidn and aggregated call duration 
    number = ""
    duration = 0
    for call in calls:
        incoming, answering, *rest, duration = call
        add_number_duration(incoming, int(duration), numbers_list)
        add_number_duration(answering, int(duration), numbers_list)

    number, duration = get_the_longest_number_duration(numbers_list)

    return print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number, duration))

longest_call(calls)
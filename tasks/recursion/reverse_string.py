def reverse_string(input):

    if len(input) == 0:
        return ""
    else:
        first_letter = input[0]
        remaining = input[1:]

        reversed_string = reverse_string(remaining)

        reversed_string = reversed_string + first_letter
        return reversed_string

print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")
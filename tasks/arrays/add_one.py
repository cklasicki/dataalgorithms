def build_number(arr):

    number = None

    if arr is None or len(arr) == 0:
        return number

    for i in range(len(arr), 0, -1):
        if number is None:
            number = 0
        number += 10**(len(arr)-i) * arr[i-1]
    return number

def convert_to_list(number: int):
    
    number_list = []

    while number != 0:
        
        number_list.append(number%10)
        number = int(number / 10)

    return number_list[::-1]

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """

    number = build_number(arr)
    number += 1

    return convert_to_list(number)


# Custom tests
assert build_number(None) == None
assert build_number([1, 2, 3]) == 123
assert build_number([0]) == 0
assert convert_to_list(123) == [1,2,3]
print('Custom tests pass')

# A helper function for Test Cases


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")


# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)

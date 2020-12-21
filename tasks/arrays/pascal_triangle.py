'''
Points to note:
1. We have to return a list.
2. The elements of n^th row are made up of elements of (n-1)^th row. This comes up till the 1^st row. We will follow a top-down approach. 
3. Except for the first and last element, any other element at position `j` in the current row is the sum of elements at position `j` and `j-1` in the previous row. 
4. Be careful about the edge cases, example, an index should never be a NEGATIVE at any point of time. 
'''


def nth_row_pascal(n):
    if n == 0:
        return [1]

    current_row = [1]

    for i in range(1, n+1):
        previous_row = current_row
        current_row = [1]
        for j in range(1, i):
            next_number = previous_row[j] + previous_row[j-1]
            current_row.append(next_number)
        current_row.append(1)
    
    return current_row

print( nth_row_pascal(10) )
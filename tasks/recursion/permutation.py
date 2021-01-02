import copy

def permute(arr):
    # print("Initial array: {}".format(arr))

    permutations_list = [[]]

    if len(arr) == 0:
        return [[]]

    if len(arr) == 1:
        permutations_list[0].append(arr[0])
        return permutations_list
    else:
        permutations_list = permute(arr[1:])
        add_next_element(arr[0], permutations_list)    
        # print("Original arr: {}, permutation arr: {}".format(arr, permutations_list))

    final_list = []
    for item in permutations_list:
        if len(item) == len(arr):
            final_list.append(item)

    # print(final_list)
    return final_list

def add_next_element(item, permutations_list):
    # print("Adding element: {}".format(item))
    all_lists = copy.deepcopy(permutations_list)
    for list in all_lists:
        for i in range(len(list) + 1):
            # print("adding {} in place {}".format(item, i))
            new_permutation = copy.copy(list)
            new_permutation.insert(i,item)
            permutations_list.append(new_permutation)
    return permutations_list

print(permute([0]))


# # Udacity solution
# # Recursive Solution 
# """
# Args: myList: list of items to be permuted
# Returns: compound list: list of permutation with each permuted item being represented by a list
# """
# import copy                                # We will use `deepcopy()` function from the `copy` module

# def permute(inputList):
    
#     # a compound list
#     finalCompoundList = []                  # compoundList to be returned 
    
#     # Terminaiton / Base condition
#     if len(inputList) == 0:
#         finalCompoundList.append([])
        
#     else:
#         first_element = inputList[0]        # Pick one element to be permuted
#         after_first = slice(1, None)        # `after_first` is an object of type 'slice' class
#         rest_list = inputList[after_first]  # convert the `slice` object into a list
        
#         # Recursive function call
#         sub_compoundList = permute(rest_list)
        
#         # Iterate through all lists of the compoundList returned from previous call
#         for aList in sub_compoundList:
            
#             # Permuted the `first_element` at all positions 0, 1, 2 ... len(aList) in each iteration
#             for j in range(0, len(aList) + 1): 
                
#                 # A normal copy/assignment will change aList[j] element
#                 bList = copy.deepcopy(aList)  
                
#                 # A new list with size +1 as compared to aList
#                 # is created by inserting the `first_element` at position j in bList
#                 bList.insert(j, first_element)
                
#                 # Append the newly created list to the finalCompoundList
#                 finalCompoundList.append(bList)
                
#     return finalCompoundList
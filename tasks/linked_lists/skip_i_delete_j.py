# ### Problem Statement

# You are given the head of a linked list and two integers, `i` and `j`.
# You have to retain the first `i` nodes and then delete the next `j` nodes. Continue doing so until the end of the linked list. 

# **Example:**
# * `linked-list = 1 2 3 4 5 6 7 8 9 10 11 12`
# * `i = 2`
# * `j = 3` 
# * `Output = 1 2 6 7 11 12` 

# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def element_to_attach(node: Node, counter: int, i: int, j: int):
    total = i + j
    if counter % total < i:
        # print("adding element " + str(node.data))
        return True
    # print("skipping element " + str(node.data))
    return False

def add_node(old_current, new_head, new_current):    
    if new_head is None:
       new_head = old_current
       new_current = new_head
    else:
        new_current.next = old_current
        new_current = new_current.next 

    return new_head, new_current

def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    
    CONCEPT:
    i nodes needs to be maintained and the j  not.
    
    - create another linked list and attach only 'i' nodes into it
    - create a subfunction that controls if a current node can be attached or not
    - return the head of the new linked list
    """
    
    old_current = head
    counter = 0

    new_head = None
    new_current = None

    while old_current is not None:
        if element_to_attach(old_current, counter, i, j):
            print('WHILE: adding element: ' + str(old_current.data))
            new_head, new_current = add_node(old_current, new_head, new_current)
        old_current = old_current.next
        counter += 1

    return new_head

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Custom tests
# assert element_to_attach(Node(1), 0, 2, 3) == True
# assert element_to_attach(Node(2), 1, 2, 3) == True
# assert element_to_attach(Node(3), 2, 2, 3) == False
# assert element_to_attach(Node(4), 3, 2, 3) == False
# assert element_to_attach(Node(5), 4, 2, 3) == False
# assert element_to_attach(Node(6), 5, 2, 3) == True
# assert element_to_attach(Node(7), 6, 2, 3) == True
# assert element_to_attach(Node(8), 7, 2, 3) == False
# assert element_to_attach(Node(9), 8, 2, 3) == False
# assert element_to_attach(Node(10), 9, 2, 3) == False
# print("Custom tests finished")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#arr = [1, 2, 3, 4, 5]
i = 2
j = 2
head = create_linked_list(arr)

skip_i_delete_j(head,i,j)

# # Solution
# """
# :param: head - head of linked list
# :param: i - first `i` nodes that are to be skipped
# :param: j - next `j` nodes that are to be deleted
# return - return the updated head of the linked list
# """
# '''
# The Idea: 
# Traverse the Linkedist. Make use of two references - `current` and `previous`.
#  - Skip `i-1` nodes. Keep incrementing the `current`. Mark the `i-1`^th node as `previous`. 
#  - Delete next `j` nodes. Keep incrementing the `current`.
#  - Connect the `previous.next` to the `current`
# '''
# def skip_i_delete_j(head, i, j):
#     # Edge case - Skip 0 nodes (means Delete all nodes)
#     if i == 0:
#         return None
    
#     # Edge case - Delete 0 nodes
#     if j == 0:
#         return head
    
#     # Invalid input
#     if head is None or j < 0 or i < 0:
#         return head

#     # Helper references
#     current = head
#     previous = None
    
#     # Traverse - Loop untill there are Nodes available in the LinkedList
#     while current:
        
#         '''skip (i - 1) nodes'''
#         for _ in range(i - 1):
#             if current is None:
#                 return head
#             current = current.next
#         previous = current
#         current = current.next
        
#         '''delete next j nodes'''
#         for _ in range(j):
#             if current is None:
#                 break
#             next_node = current.next
#             current = next_node
        
#         '''Connect the `previous.next` to the `current`''' 
#         previous.next = current
    
#     # Loop ends
    
#     return head
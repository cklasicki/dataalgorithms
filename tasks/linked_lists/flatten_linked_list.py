# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones.
# User defined class
class Node:
    def __init__(self, value):  # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None

    def __repr__(self):
        
        if isinstance(self.value, LinkedList):
            return "linkedList"
        else:
            return str(self.value)

# User defined class


class LinkedList:
    def __init__(self, head):  # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''

    def __repr__(self):
        return self.to_list()

    def append(self, value):

        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

    '''We will need this function to convert a LinkedList object into a Python list of integers'''

    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:       # <-- Iterate untill we have nodes available
            # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            out.append(int(str(node.value)))
            node = node.next

        return out

    def size(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length


def merge(list1: LinkedList, list2: LinkedList):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''    

    merged = LinkedList(None)

    if list1 is None:
        return list2
    if list2 is None:
        return list1

    list1_elem = list1.head
    list2_elem = list2.head

    while list1_elem is not None or list2_elem is not None:
        if list1_elem is None or list1_elem.value > list2_elem.value:
            merged.append(list2_elem)
            list2_elem = list2_elem.next
        elif list2_elem is None or list1_elem.value <= list2_elem.value:
            merged.append(list1_elem)
            list1_elem = list1_elem.next

    return merged

''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''

class NestedLinkedList(LinkedList):
    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.

        main_current = self.head
        while main_current is not None:
            print(main_current)
            mergedList = merge(main_current, main_current.value)
            main_current = main_current.next
        
        return self


# Custom Tests 
ll1 = LinkedList(Node(1))
ll1.append(2)
ll2 = LinkedList(Node(10))

merged = merge(ll1, ll2)

assert merged.size() > 0 or 'Fail'

print("Tests finished.")

# First Test scenario
''' Create a simple LinkedList'''
linked_list = LinkedList(
    Node(1))  # <-- Notice that we are passing a Node made up of an integer
# <-- Notice that we are passing a numerical value as an argument in the append() function here
linked_list.append(3)
linked_list.append(5)

''' Create another simple LinkedList'''
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''
nested_linked_list = NestedLinkedList(Node(
    linked_list))  # <-- Notice that we are passing a Node made up of a simple LinkedList object
# <-- Notice that we are passing a LinkedList object in the append() function here
nested_linked_list.append(second_linked_list)

solution = nested_linked_list.flatten() # <-- returns A LinkedList object

expected_list = [1,2,3,4,5] # <-- Python list

# Convert the "solution" into a Python list and compare with another Python list
assert solution.to_list() == expected_list, f"list contents: {solution.to_list()}"

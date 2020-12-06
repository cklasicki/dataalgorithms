class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head

# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend

def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here
    
    if self.head is None:
        self.head = Node(value)
    else:
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = Node(value)
    
LinkedList.append = append

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
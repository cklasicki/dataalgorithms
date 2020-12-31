class Queue:
    
    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        # TODO: Check if the queue is full; if it is, call the _handle_queue_capacity_full method
        if self.queue_size == len(self.arr):
            self._handle_queue_capacity_full()
        
        # enqueue new element
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        # check if queue is empty
        if self.is_empty():
            self.front_index = -1   # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0
    
    def front(self):
        # check if queue is empty
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    # TODO: Add the _handle_queue_capacity_full method
    def _handle_queue_capacity_full(self):
        
        # copy all values to the temp arr
        old_arr = self.arr
        
        # resizing array
        self.arr = [0 for _ in range(2 * len(self.arr))]
        
        # copy all items from the head to the new array
        
        index = 0
        
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1
        
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1
        
        self.front_index = 0
        self.next_index = index
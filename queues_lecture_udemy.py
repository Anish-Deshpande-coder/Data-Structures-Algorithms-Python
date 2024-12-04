class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value):
        self.head = None
        self.tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
        
    def enqueue(self, value):
        new_node = Node(value)
        if not self._size: #checks if list is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return self
    
    def dequeue(self):
        if not self._size:
            raise Exception("queue is empty")
        former_head = self.head
        self.head = former_head.next
        removed_item.next = None
        self._size -= 1
        if not self._size:
            self.tail = None
        return former_head.value
    
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        return self
    
    def peek(self):
        if self._top:
            return self._top.value
        return None
    
    
    
    
    
    












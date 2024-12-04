class ArrayStack:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
    
    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()


class Queue:
    def __init__(self):
        self.in_stack = ArrayStack()
        self.out_stack = ArrayStack()
    
    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()
    
    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)
    
    def enqueue(self, e):
        self.in_stack.push(e)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.top()
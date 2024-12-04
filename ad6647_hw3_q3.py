from collections import deque

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


class MidStack:
    def __init__(self):
        self.stack = ArrayStack() 
        self.deque = deque()   
    
    def is_empty(self):
        return self.stack.is_empty() and not self.deque
    
    def __len__(self):
        return len(self.stack) + len(self.deque)
    
    def push(self, e):
        self.stack.push(e)
    
    def top(self):
        if self.stack.is_empty():
            raise Exception("Stack is empty")
        return self.stack.top()
    
    def pop(self):
        if self.stack.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()
    
    def mid_push(self, e):
        n = len(self)
        for i in range(n // 2):
            self.deque.appendleft(self.stack.pop())
        self.stack.push(e)
        while self.deque:
            self.stack.push(self.deque.popleft())
            
            
            
            
            
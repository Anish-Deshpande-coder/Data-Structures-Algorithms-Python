class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
class MaxBinaryHeap:
    def __init__(self):
        self.items = []
    
    def insert(self, value):
        self.items.append(value)
        self.move_up()
        return self
        #Time: O(logn)
        #Space: O(1)
    
    def move_up(self):
        child_idx = len(self.items) - 1
        while child_idx > 0:
            parent_idx = (child_idx - 1) // 2
            if self.items[child_idx] <= self.items[parent_idx]:
                break
            self.swap(child_idx, parent_idx)
            child_idx = parent_idx
                
    def swap(self, idx_1, idx_2):
        self.items[idx_1], self.items[idx_2] = self.items[idx_2], self.items[idx_1]
        
    def remove_max(self):
        if not self.items:
            raise Exception("Heap is empty")
        max_elem = self.items[0]
        end_idx = len(self.items) - 1
        self.swap(0, end_idx)
        self.items.pop()
        self.move_down
        return max_elem
        
    def move_down(self):
        parent_idx = 0
        child_idx = 2 * parent_idx + 1
        end_idx = len(self.items) - 1
        while child_idx <= end_idx:
            if child_idx < end_idx and self.items[child_idx] < self.items[child_idx + 1]:
                child_idx += 1
            if self.items[parent_idx] < self.items[self.items]:
                self.swap(parent_idx, child_idx)
                parent_idx = child_idx
                child_idx = 2 * parent_idx + 1
            else:
                break
            
    def heapify(array):
        last_parent_idx = len(array) // 2 - 1
        for idx in range(last_parent_idx, -1, -1):
            move_down(array, idx, len(array) - 1)
        return array
        
        def move_down(array, start_idx, end_idx):
            child_idx = 2 * start_idx + 1
            while child_idx <= end_idx:
                if child_idx < end_idx and array[child_idx] < array[child_idx + 1]:
                    child_idx += 1
                if array[start_idx] < array[child_idx]:
                    array[start_idx], array[child_idx] = array[child_idx], array[start_idx]
                    start_idx = child_idx
                    child_idx = 2 * start_idx + 1
                else:
                    break
        #Time: O(n)
        #Space: O(1)
        
            
        
        
        
        
        
        
        
                
                
                
                
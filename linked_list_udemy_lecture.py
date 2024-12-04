#singly-linked list code

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0
    
    def append(self, value): #append method
        new_node = Node(value)
        if not self._length: #checks if list is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1
        return self
    #time: O(1)
    #space: O(1)
    
    def prepend(self, value):
        new_node = Node(value)
        if not self._length: #checks if list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._length += 1
        return self
    #time: O(1)
    #space: O(1)
        
    def pop_left(self):
        if not self._length:
            raise Exception("list is empty")
        former_head = self.head
        self.head = former_head.next
        removed_item.next = None
        self._length -= 1
        if not self._length:
            self.tail = None
        return former_head.value
    #time: O(1)
    #space: O(1)
    
    def pop_right(self):
        if not self._length:
            raise Exception("list is empty")
        tail_value = self.tail.value
        if self._length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = None
        self._length -= 1
        return tail_value
    #time: O(n)
    #space: O(1)
    
    def remove(self, value):
        if not self._length:
            raise Exception("list is empty")
        if self.head.value == value:
            return self.pop_left()
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            raise ValueError("item not in list")
        if current_node.next is None:
            self.tail = previous_node
        previous_node.next = current_node.next
        current_node.next = None
        self._length -= 1
        return current_node.value
    #time: O(n)
    #space: O(1)
    
    def reverse(self):
        if self._length < 2:
            return self
        left_node = None
        middle_node = self.head
        while middle_node is not None:
            right_node = middle_node.next
            middle_node.next = previous_node
            left_node = middle_node
            middle_node = right_node
        self.head, self.tail = self.tail, self.head
        return self
    #time: O(n)
    #space: O(1)
    
my_list = SinglyLinkedList()
my_list.append(3)
my_list.append(5)

print(my_list)
print(my_list.head) #to access the value at head or tail do print(my_list.head.value)
print(my_list.tail)
print(my_list._length)
 

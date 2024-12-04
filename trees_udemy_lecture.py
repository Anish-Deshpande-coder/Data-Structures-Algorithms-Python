class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return self
        current_node = self.root
        while value != current_node.value:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    break
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    break
                current_node = current_node.right
        return self
        # Space: O(1)
        # Time: O(logn) best case scenario, O(n) worst case scenario
        
        
    def contains(self, value):
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return True
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
        # Space: O(1)
        # Time: O(logn) best case scenario, O(n) worst case scenario
        
    def remove(self, value, start = None, parent = None):
        current = start or self.root
        while current and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        if not current:
            raise Exception("item not in tree")
        if not current.right and not current.left:
            return self._remove_node_no_children(current, parent)
        if current.right and current.left:
            return self._remove_node_two_children(current, parent)
        else:
            return self._remove_node_one_child(current, parent)

        
        
    def remove_node_no_children(self, current, parent):
        if current.value == self.root:
            self.root = None
            return self
        if parent.left == current:
            parent.left = None
        else:
            parent.right = None
        return None
    
    def _remove_node_one_child(self, current, parent):
        if current.value == self.root:
            if current.right:
                self.root = current.right
            else:
                self.root = current.left
            return self
        if parent.right = current:
            if current.right:
                parent.right = current.right
            else:
                parent.right = current.left
        else:
            if current.right:
                parent.left = current.right
            else:
                parent.left = current.left
        return self
    
    def _remove_node_two_children(self, current)
        successor = self._get_successor(current)
        current.value = successor.value
        return self.remove(successor.value, start = current.right, parent = currennt)
        
    def _get_successor(current):
        sucessor = current.right
        while successor and successor.left:
            successor = successor.left
        return successor
    
        # Space: O(1)
        # Time: O(logn) best case scenario, O(n) worst case scenario
    
    








from DoublyLinkedList import DoublyLinkedList

class CompactString:
    def __init__(self, orig_str):
        self.compact_list = DoublyLinkedList()
        self._compress_string(orig_str)

    def _compress_string(self, orig_str):
        if not orig_str:
            return
        current_char = orig_str[0]
        count = 1
        for char in orig_str[1:]:
            if char == current_char:
                count += 1
            else:
                self.compact_list.add_last((current_char, count))
                current_char = char
                count = 1
        self.compact_list.add_last((current_char, count))

    def __add__(self, other):
        new_compact = CompactString("")
        new_compact.compact_list = DoublyLinkedList()
        for node in self.compact_list:
            new_compact.compact_list.add_last(node)
        for node in other.compact_list:
            last_node = new_compact.compact_list.trailer.prev.data
            if last_node[0] == node[0]:
                merged_node = (last_node[0], last_node[1] + node[1])
                new_compact.compact_list.delete_last()
                new_compact.compact_list.add_last(merged_node)
            else:
                new_compact.compact_list.add_last(node)
        return new_compact

    def __lt__(self, other):
        return self._compare(other) > 0

    def __le__(self, other):
        return self._compare(other) >= 0

    def __gt__(self, other):
        return self._compare(other) < 0

    def __ge__(self, other):
        return self._compare(other) <= 0

    def _compare(self, other):
        self_iter = iter(self.compact_list)
        other_iter = iter(other.compact_list)
        while True:
            try:
                self_char, self_count = next(self_iter)
            except StopIteration:
                self_char, self_count = None, 0
            try:
                other_char, other_count = next(other_iter)
            except StopIteration:
                other_char, other_count = None, 0
            if self_char is None and other_char is None:
                return 0 
            if self_char is None:
                return -1  
            if other_char is None:
                return 1  
            if self_char != other_char:
                return -1 if self_char < other_char else 1
            if self_count != other_count:
                return -1 if self_count < other_count else 1

    def __repr__(self):
        result = []
        for char, count in self.compact_list:
            result.append(char * count)
        return ''.join(result)
    
    
    
    
    
    
    
    
    
    
    
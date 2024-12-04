from copy import copy
from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    new_lnk_lst = DoublyLinkedList() 
    current = lnk_lst.header.next
    while current != lnk_lst.trailer:
        new_lnk_lst.add_last(current.data)
        current = current.next
    return new_lnk_lst

def deep_copy_linked_list(lnk_lst):
    new_lnk_lst = DoublyLinkedList()
    current = lnk_lst.header.next
    while current != lnk_lst.trailer:
        if isinstance(current.data, DoublyLinkedList):
            nested_copy = deep_copy_linked_list(current.data)
            new_lnk_lst.add_last(nested_copy)
        else:
            new_lnk_lst.add_last(current.data)
        current = current.next
    return new_lnk_lst

    
    
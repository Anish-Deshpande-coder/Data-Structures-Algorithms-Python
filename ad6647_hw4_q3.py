from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    merged_list = DoublyLinkedList()
    
    def merge_sublists(node1, node2):
        if node1 is srt_lnk_lst1.trailer and node2 is srt_lnk_lst2.trailer:
            return
        if node1 is srt_lnk_lst1.trailer:
            merged_list.add_last(node2.data)
            return merge_sublists(node1, node2.next)
        if node2 is srt_lnk_lst2.trailer:
            merged_list.add_last(node1.data)
            return merge_sublists(node1.next, node2)
        if node1.data <= node2.data:
            merged_list.add_last(node1.data)
            merge_sublists(node1.next, node2)
        else:
            merged_list.add_last(node2.data)
            merge_sublists(node1, node2.next)
    merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next)
    return merged_list
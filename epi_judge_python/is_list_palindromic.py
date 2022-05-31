from turtle import back
from list_node import ListNode
from test_framework import generic_test

# My solution
def is_linked_list_a_palindrome(L: ListNode) -> bool:
    def length(L : ListNode):
        length = 0
        while L:
            L = L.next
            length += 1
        return length
    
    # Less than 3
    original_list_length = length(L)
    if not L or original_list_length < 3:
        return True

    # 3
    if original_list_length == 3:
        return L.data == L.next.next.data

    # More than 3
    sublist_head = L.next if original_list_length % 2 else L
    for _ in range((original_list_length // 2) - 1):
        sublist_head = sublist_head.next
    
    sublist_end = sublist_head.next
    tmp = None
    for _ in range((original_list_length // 2) - 1):
        tmp = sublist_end.next
        sublist_end.next = tmp.next
        tmp.next = sublist_head.next
        sublist_head.next = tmp

    for _ in range(original_list_length // 2):
        if L.data != tmp.data:
            return False
        L, tmp = L.next, tmp.next
    return True


if __name__ == '__main__':
    # exit(
    #     generic_test.generic_test_main('is_list_palindromic.py',
    #                                    'is_list_palindromic.tsv',
    #                                    is_linked_list_a_palindrome))
    L = ListNode()
    reverse_list(L)
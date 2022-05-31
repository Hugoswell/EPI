from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# My solution
def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    even = even_iter = ListNode()
    odd = odd_iter = ListNode()

    i = 0
    while L:
        if i % 2:
            odd_iter.next = L
            odd_iter = odd_iter.next
        else:
            even_iter.next = L
            even_iter = even_iter.next
        L = L.next
        i += 1
    
    odd_iter.next = None
    even_iter.next = odd.next
    return even.next

# EPI solution
def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    even_dummy_head, odd_dummy_head = ListNode(), ListNode
    tails, swap = [even_dummy_head, odd_dummy_head], 0

    while L:
        tails[swap].next = L
        L = L.next
        tails[swap] = tails[swap].next
        swap ^= 1
    tails[1].next = None
    tails[0].next = odd_dummy_head.next
    return even_dummy_head.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))

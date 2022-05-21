from multiprocessing import dummy
from re import sub
from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummy = sublist_head = ListNode(next = L)
    
    for _ in range(1, start):
        sublist_head = sublist_head.next
    sublist_first = sublist_head.next

    for _ in range(finish - start):
        tmp = sublist_first.next
        sublist_first.next = tmp.next
        tmp.next = sublist_head.next
        sublist_head.next = tmp

    return dummy.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))

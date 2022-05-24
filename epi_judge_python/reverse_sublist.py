from multiprocessing import dummy
from re import sub
from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummy = head = ListNode(next=L)

    for _ in range(1, start):
        head = head.next
    end = head.next

    for _ in range(finish - start):
        iter = end.next
        end.next = iter.next
        iter.next = head.next
        head.next = iter
    
    return dummy.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))

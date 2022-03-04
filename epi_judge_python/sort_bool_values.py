from typing import List

def sort_bool_values(A : List[bool]) -> None:
    print(A)
    smaller = 0
    for i in range(len(A)):
        if A[i] is False:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    print(A)

A = [True,True,False,True,False,True,True,True,False,True,False,True]
sort_bool_values(A)
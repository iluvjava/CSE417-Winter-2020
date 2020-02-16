"""
Class: Cse 417
Name: Hongda Li

This is a file prepared for cse417 winter 2020 HW6 assignment. It contains some examples and investigations
on divide and conquer algorithms.
"""
__all__ = []

from typing import List
from random import random as rnd

def k_larges(A:List[int], k: int):
    """
        Returns the Kth largest element in the array.
    :param A:
        The Array.
    :param k:
        The kth index of the element, k = 1 will mean you want the smallest elements
        in the array.
    :return:
        The kth largest elements in the array.
    """
    if k <= 0 or k > len(A):
        return None
    if k == 1 or k == len(A):
        return A[k - 1]
    pivot = A[int(len(A)*rnd())]
    smaller_strict = []
    larger = []

    for I in A:
        choice = smaller_strict if I < pivot else larger
        choice.append(I)
    del choice, I

    if len(smaller_strict) == k - 1:
        return pivot
    if len(smaller_strict) >= k:
        return k_larges(smaller_strict, k)
    return k_larges(larger, k - len(smaller_strict))


def varify(N = 10):
    A = [int(7*rnd()) for I in range(10)]
    B = (A[:])
    B.sort()
    for I in range(10):
        if B[I] != k_larges(A, I + 1):
            return False
    return True


if __name__ == "__main__":
    print(k_larges([1,4,2,6,7,9], 3))
    print(k_larges([1,1,1,2,2,3,3,3], 4))
    print(varify())
    pass
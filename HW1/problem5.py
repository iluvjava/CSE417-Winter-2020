"""
Name: Hongda Li
Class cse 417
This file is for hw1, problem 5.
* Codes require python 3.6 or above.
* Codes requires solutions of problem 4.
! Codes are slow cause it's written in python.

Here are the definition for some of the keywords listed in problem 5:
m.rank() -> The choice of m after the perfect matching algorithms.
M.goodness -> sum_{i=0}^{n-1}m.rank()/n
"""
from typing import List, Tuple
from random import random
from problem4 import convert, produce_stable_match


def rand_permutation(arr: List)-> List:
    """
    :param arr:
    A array with elements.
    :return:
    A new randomly permutated array from arr.
    """
    newarr = arr.copy()
    for I in range(len(newarr)):
        J = int(random()*I)
        newarr[I], newarr[J] = newarr[J], newarr[I]
    return newarr

def get_goodness(arr: List[int], M: List[List], W: List[List])->Tuple:
    """
    Function will return the measure of goodness for both the, M and W using the returned results gotten
    from problem 4.
    :param arr:
        The results produced from problem 4.
    :param M:
        The preference matrix for M.
    :param W:
    :return.
        A tuple where the first element is the goodness for M and the second is the goodness for W.
    """
    M_psum = 0
    W_psum = 0
    M_tbl = convert(M)
    W_tbl = convert(W)
    l = len(arr)
    assert arr is not None, "Why are you passing None to this function? "
    for E, I in zip(arr, range(len(arr))):
        M_psum += M_tbl[I][1][E] + 1
        W_psum += W_tbl[E][1][I] + 1
    return (M_psum/l, W_psum/l)


def goodness_for_random_preferences():
    """
    Function will generate a randomly permutated lists for the preferece list for M, W, then it
    will measure the goodness for W, and M, with an n starting at 1000, increments at 100 and ends at 1e4
    :return:
    """
    for N in range(10**3, 10**4, 100):
        lst = list(range(N))
        M = [rand_permutation(lst) for I in range(N)]
        W = [rand_permutation(lst) for I in range(N)]
        goodness = get_goodness(produce_stable_match(M, W, verbo=False), M, W)
        print(f"N = {N}; Goodeness = {goodness}")
    return


if __name__ == "__main__":
    print("Let's test something first before running everything else. ")
    print("All m has the same preference list for w while w has random preference list: ")
    n = 100
    R = list(range(n))
    M = [R for I in range(n)]
    W = [rand_permutation(R) for I in range(n)]
    result = produce_stable_match(M, W, verbo=False)
    print(result)
    goodness = get_goodness(result, M, W)
    assert goodness[0] == 5050/100, "Ok, there is something wrong please check. "
    print("Ok, for the special cause proved in problem 1, the codes seem to work. ")
    print("Running on random input, we have the following values for goodness: ")
    goodness_for_random_preferences()


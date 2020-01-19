"""
Name: Hongda Li
Class: Cse 417 winter 2020

This file contains codes written for HW2 problem 5, 6 of the class cse 417. It has the basic set up for the coupon collector
simulations.
I personally love python (for completing HW), among all the languages I used, C#, MATLAB, JAVA,
or EVEN javascript, python is the easiest for completing HW.
"""
from random import random
R = random

def coupon_simulate(N:int = 100, include_arr = False):
    """
        Function simulate the coupon problem for a certain size: N
    :param N:
        The problem size.
    :return:
        The total number of coupon received such that coupons of every type are
        collected at least once.
    """
    my_collection = [None]*N
    def rnd():
        return int(R()*N)
    remaining = N
    while remaining != 0:
        r = rnd()
        if my_collection[r] is None:
            remaining -= 1
            my_collection[r] = 1
            continue
        my_collection[r] += 1
    return sum(my_collection) if not include_arr else (sum(my_collection), my_collection)

def fancy_coupon_simulate(N: int = 100):
    """
        This function is designed for problem 5.
        Coupons will have a random value in 0 to n-1, and there are still n types of coupons.
        The collection will choose the coupon with the minimum value for each type of coupons.
    :param N:
        The number of types of coupons.
    :return:
        The average value when we have a complete set of coupons!
    """
    my_Collection = [None]*N
    def random_coupon():
        return int(R()*N), int(R()*N) + 1
    remaining = N
    while remaining != 0:
        c, v = random_coupon()
        if my_Collection[c] is None:
            remaining -= 1
            my_Collection[c] = v
            continue
        if my_Collection[c] > v:
            my_Collection[c] = v
    return sum(my_Collection)


if __name__ == "__main__":
    print("Testing the average coupon need for size of 4000, repeating 20 times. ")
    N = [125, 250, 500, 1000, 2000, 4000, 8000]
    n = 50
    total = [sum(coupon_simulate(J) for I in range(n))/n for J in N]
    results = [(x, x/I) for x, I in zip(total, N)]
    print(f"results: \n {results}")
    print("Let's make it easier for LaTeX formatting: ")
    print("\\begin{tabular}{|c|c|c|c|}")
    print("\t$C$ & $C/n$ & $N$\\hline\\\\")
    for z, N in zip(results, N):
        x, y = z
        print(f"\t{x} & {y} & {N}\\\\\\hline")
        pass
    print("\\end{tabular}")
    print("Looks similar to the M-rank for perfect matching... ")

    print("Now, let's run the fancier coupon collector and see what kinda of value it can create. ")
    N = [125, 250, 500, 1000, 2000, 4000, 8000]
    total = [sum(fancy_coupon_simulate(J) for I in range(n))/n for J in N]
    results = [(x, x/I) for x, I in zip(total, N)]
    print(results)
    print(f"results: \n {results}")
    print("Let's make it easier for LaTeX formatting: ")
    print("\\begin{tabular}{|c|c|c|c|}")
    print("\\hline")
    print("\t$V$ & $V/n$ & $N$\\hline\\\\")
    for z, N in zip(results, N):
        x, y = z
        print(f"\t{x} & {y} & {N}\\\\\\hline")
        pass
    print("\\end{tabular}")
    print("Looks similar to the W-rank for perfect matching... ")
"""
Class: Cse 417
Name: Hongda Li

This is a file prepared for cse417 winter 2020 HW6 assignment. It contains some examples and investigations
on divide and conquer algorithms.

* This file is going to present all the data onto the console.
* Python 3.7 or above is needed
*

"""
__all__ = ["CodesAnalysis"]

from typing import List
from random import random as rnd
from random import shuffle
from numpy import *
import matplotlib.pyplot as plt


class CodesAnalysis:
    """
        The is a class that can help with collecting data about the performance of the
        k_th largest elements in the array function.

        I am going to up all the date relevant to analysis into one class.
        Then I am attaching the static method as an instance method of this class.

        ! The test will only use randomized array without repeating elements.

        TestInstance:
        [ (inputsize, comparison), (inputsize, comparison)... (inputsize, comparison)]

        * When running an random test instance of  the k_th largest method, it will attach all the info about it
        at the end of the array, making it easier for analysis of the method. 
    """

    def __init__(self):
        self.__AnalysisData = []
        pass

    def __rnd_arr(self, N):
        res =  list(range(N))
        shuffle(res)
        return res

    def register(self, N):
        counter = [0]
        def k_th_inner(A: List[int], k):
            assert k >= 1 and k <= len(A), "Invalid k or array."
            pivot = A[int(rnd() * len(A))]
            equalTo = []
            larger = []
            smaller = []
            for I in A:
                choice = equalTo if I == pivot else (larger if I > pivot else smaller)
                choice.append(I)
                counter[0] += 1
            del I, choice
            if len(smaller) == k - 1:
                return pivot
            if len(smaller) < k:
                return pivot if k - len(smaller) < len(equalTo) else \
                    k_th_inner(larger, k - len(equalTo) - len(smaller))
            if len(smaller) >= k:
                return k_th_inner(smaller, k)
        # Run and record the data.
        RndArr = self.__rnd_arr(N)
        k_th_inner(RndArr, int(rnd()*len(RndArr)) + 1)
        self.__AnalysisData.append((N, counter[0]))

    def analyze(self):
        """
        Function will use all info registered to analyze the
        constraint time factor involved in the randomized median algorithm.
        :return:
        [(N, averageComparisons), (N, averageComparisons) ... ]
        """
        average = {}
        for N, C in self.__AnalysisData:
            if N not in average.keys():
                average[N] = (C, 1)
                continue
            average[N] = (average[N][0] + C, average[N][1] + 1)
        return [(Size, C[0]/C[1]) for Size, C in average.items()]


def k_th(A: List[int], k):
    """
        For this method, I have to consider repeating
        elements in the array to feel a sense of closure when designing algorithm.

    :param A:
        The array of integers.
    :param k:
        The rank of the elements you want.
        Starting with 1 and no more than the length of the array.
    :return:
        The kth rank element in the array.
    """
    assert k >= 1 and k <= len(A), "Invalid k or array."
    pivot = A[int(rnd()*len(A))]
    equalTo = []
    larger = []
    smaller = []
    for I in A:
        choice = equalTo if I == pivot else (larger if I > pivot else smaller)
        choice.append(I)
    del I, choice
    if len(smaller) == k - 1:
        return pivot
    if len(smaller) < k:
        return pivot if k - len(smaller) < len(equalTo) else \
            k_th(larger, k - len(equalTo) - len(smaller))
    if len(smaller) >= k:
        return k_th(smaller, k)


def test2():
    repeats = 1000
    while repeats >= 0:
        N = 20
        A = [int(rnd()*N*0.7) for I in range(N)]
        B = A.copy()
        B.sort()
        assert min(B) == k_th(A, 1)
        repeats -= 1
    print("Test2 finished ")


def test3():
    repeats = 10
    while repeats >= 0:
        N = 20
        A = [int(rnd() * N * 0.7) for I in range(N)]
        B = A.copy()
        B.sort()
        for I, E in zip(range(1, len(B) + 1), B):
            try:
                assert E == k_th(A, I)
            except:
                print(f"Failed on inputs:")
                print(f"A: {A}")
                print(f"B: {B}")
                print(f"I: {I}")
                print(f"E: {E}")
                return
        repeats -= 1


def test4():
    repeats = 1000
    while repeats >= 0:
        N = 200
        RandomArr = [int(rnd() * N * 0.7) for I in range(N)]
        Sorted = RandomArr.copy()
        Sorted.sort()
        for element, position in zip(Sorted, range(len(Sorted))):
            try:
                Klargest = k_th(RandomArr, position + 1)
            except:
                # debugg
                pass
            if Klargest != element:
                pass
        repeats -= 1
    print("Test4 finished. ")


def run_codes_analysis():
    TestInstance = CodesAnalysis()
    repeatition = 30
    for I in range(repeatition):
        print("\r", end=f"{int((I/repeatition)*100)}%")
        for N in range(100, 10000, 100):
            TestInstance.register(N)
    print()
    stats = TestInstance.analyze()

    # Print out the results for the problem and determine the line of best fits.
    X_data = []
    Y_data = []
    for X, Y in stats:
        X_data.append(X)
        Y_data.append(Y)

    c = polyfit(X_data, Y_data, 1)
    BestFit = polyval(c, X_data)
    plt.plot(X_data, Y_data, "ro")
    plt.plot(X_data, BestFit)
    plt.title(f"The slope is: {c[0]}")
    plt.savefig("HW6Q5")
    print(f"Polyval results Show that the constant factor is: {c[0]}")


def main(repeats = 1000):
    while repeats != 0:
        A = list(range(1, 11))
        shuffle(A)
        for I in A:
            assert I == k_th(A, I)
        repeats -= 1
    print("Main function finished executing. ")


if __name__ == "__main__":
    # print(k_th([1,4,2,6,7,9], 3))
    # print(k_th([1,1,1,2,2,3,3,3], 4))
    # print(k_th([1, 6, 0, 5, 3, 4, 5, 0, 2, 1], 1))
    # print("-----------Randomized Testing-----------")
    # main()
    # test2()
    # test4()
    # print("All tests passed. ")
    run_codes_analysis()
    pass




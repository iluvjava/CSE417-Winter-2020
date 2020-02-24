"""

name: hongda li
class: cse 417 winter 2020.
This file meant for demonstrating dynamic programing for interval scheduling.
"""
__all__ = ["random_interval_generator", "greedy1", "greedy2", "dp_solution"]

from random import random as rnd
from copy import deepcopy


def random_interval_generator(n, L, r):
    """
    Random return an array of interval, starting position chosen from [1, L]
    Length uniformly chosen frm [1, r]
    :param L:
        The range of interval lies in, L must be larger than 1, cause the
        left endpoint of the range is 1.
    :param r:
        The length of the intervals. It must be larger than 1 too.
    :return:
        A list of tuples, each tuple representing an interval.
        The list of random intervals will be sorted by the starting time too.
    """
    assert L > 1 and r > 1 and n >= 1, "Invalid parameters"
    TupleList = [None]*n
    for I in range(n):
        Starting = 1 + rnd()*L
        Length = 1 + rnd()*r
        TupleList[I] = (Starting, Starting + Length)
    return TupleList


def greedy1(intervals):
    """
        This greedy algorithm attempts to maximize the total length of the intervals
        selected from the set of intervals.
        It will sort intervals according to starting time and then selected the
        intervals with the earliest starting time without any cause of conflicts.
    :return:
        A list of intervals as solution.
    """
    intervals = deepcopy(intervals)
    Optimal = [intervals[0]]
    sorted(intervals, key=lambda x: x[0])
    for Startingtime, Endingtime in intervals:
        if Startingtime > Optimal[-1][1]:
            Optimal.append((Startingtime, Endingtime))
    return Optimal


def greedy2(intervals):
    """
        This is a greedy algorithm that selects intervals with longest length.
        * It will first sort all the intervals in staring time
        * It will select intervals with the longest duration that is without conflicts.
    :param intervals:
        A set of tuples representing intervals.
    :return:
        A list of intervals.
    """
    intervals = deepcopy(intervals)
    sorted(intervals, key=lambda x : -(x[1] - x[0]))
    Optimal = [intervals[0]]
    for Starting, Finishing in intervals:
        if Starting > Optimal[-1][1]:
            Optimal.append((Starting, Finishing))
    return Optimal


def dp_solution(intervals):
    """
        This is a dynamic programming solution that maximizes the sum of the the
        total interval length.
        There won't be conflicts in the solution.
    NOTE:
        If 2 intervals are touching, they are viewed as conflicting.
    :param intervals:
        A list of tuple representing the intervals.
    :return:
        A list of intervals without any intersection, and the sum of their length will be the
        biggest possible.
    """

    intervals = deepcopy(intervals)
    sorted(intervals, key=lambda x: x[1])
    Unconflicted = [0]
    OptObjectiveVal = [0] # Objective Value
    Optimal = [[]] # Solution, 2D array.

    # Establish unconflicted interval with largest finishing time for each of the interval.
    for I, Interval in enumerate(intervals):
        if I == 0:
            continue
        for J in range(I - 1, -1, -1):
            if intervals[J][1] < Interval[0]:
                Unconflicted.append(J + 1)
                break
            if J == 0 and intervals[0][1] > Interval[0]:
                Unconflicted.append(0)

    for I, Interval in enumerate(intervals):
        OptimalInclude = OptObjectiveVal[Unconflicted[I]] + Interval[1] - Interval[0]
        OptimalExclude = OptObjectiveVal[-1]
        if OptimalExclude > OptimalInclude:
            OptObjectiveVal.append(OptimalExclude)
            Optimal.append(Optimal[-1])
        else:
            OptObjectiveVal.append(OptimalInclude)
            Optimal.append(Optimal[Unconflicted[I]] + [Interval])

    return Optimal, OptObjectiveVal[-1]


def test_dynamic_programming():
    TestIntervals = [(0,4),(5,9),(3,8)]
    OptimalSoln, OptimalValue = dp_solution(TestIntervals)
    print(f"Optimal Soln is: {OptimalSoln}")
    print(f"Optimal Value is: {OptimalValue}")

    TestIntervals = [(0, 4), (5, 9), (9.5, 10), (11, 15)]
    OptimalSoln, OptimalValue = dp_solution(TestIntervals)
    print(f"Optimal Soln is: {OptimalSoln}")
    print(f"Optimal Value is: {OptimalValue}")

    TestIntervals = [(0, 4), (5, 9), (9.5, 10), (-6, 15)]
    OptimalSoln, OptimalValue = dp_solution(TestIntervals)
    print(f"Optimal Soln is: {OptimalSoln}")
    print(f"Optimal Value is: {OptimalValue}")

    print("Check above printout by eyes and hands to confirm correctness.")
    pass


def main():
    L = 4
    r = 4
    n = 10
    print(random_interval_generator(n, L, r))
    test_dynamic_programming()
    print("In theory, if the intervals are non overlapping, we should have the same results for all algorithms. ")

    testintervals = list(zip(range(0, 100, 10), range(1, 101, 10)))
    print(testintervals)

    print(dp_solution(testintervals)[1])
    g1 = greedy1(testintervals)
    Sum = 0
    for S,F in g1:
        Sum += F - S
    g1 = Sum
    g2 = greedy2(testintervals)
    Sum = 0
    for S, F in g2:
        Sum += F - S
    g2 = Sum
    print(f"g1: {g1}; g2: {g2}")
    pass

if __name__ == "__main__":
    print("File has been run. ")
    print("Randomly generating some intervals. ")
    main()

    pass
"""
name: Hongda li
class: CSE 417 Winter 2020
Testing the performance for different algorithms in dynamic_programing.py

"""

from dynamic_programming import *

class ComparingPerformance:

    def __init__(self):

        self.__Greedy1ObjectiveValues = []
        self.__Greedy2ObjectiveValues = []
        self.__DynamicObjectiveValues = []

    def runit(self):
        n = 10 ** 3
        L = 10 ** 5
        r = 2 * 10 ** 2
        test_intervals = random_interval_generator(n, L, r)
        self.__DynamicObjectiveValues.append(dp_solution(test_intervals)[1])

        opt = greedy1(test_intervals)
        Sum = 0
        for S, F in opt:
            Sum += F - S
        self.__Greedy1ObjectiveValues.append(Sum)

        opt = greedy2(test_intervals)
        for S, F in opt:
            Sum += F - S
        self.__Greedy2ObjectiveValues.append(Sum)

    def produce_avg_results(self):
        g1 = self.__Greedy1ObjectiveValues
        g2 = self.__Greedy2ObjectiveValues
        dp = self.__DynamicObjectiveValues
        return sum(g1)/len(g1), sum(g2)/len(g2), sum(dp)/len(dp)

    def get_results_list(self):
        
        pass

def main():
    N = 50
    instance = ComparingPerformance()
    while N >= 1:
        print(f"\r{N}", end="")
        instance.runit()
        N -= 1
    print(instance.produce_avg_results())






if __name__ == "__main__":
    main()
    pass
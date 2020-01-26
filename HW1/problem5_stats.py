"""
    name: Hongda Li
    class; CSE 417

    This file is going to perform linear regression and obtain some stats from the outputs from problem 5.
"""

Data = [(4.92048, 25.2448), (6.008319999999998, 41.97607999999998), (6.659639999999999, 76.63016000000002),\
(7.445580000000001, 136.68726), (8.089469999999999, 253.58859000000004), (8.919784999999997, 456.4239599999999),\
 (9.735907500000001, 837.95485)]
N = [125, 250, 500, 1000, 2000, 4000, 8000]
from math import log

if __name__ == "__main__":
    print("We are trying to linear fit the data point. ")
    Y1 = [x for x, y in Data]
    Y2 = [y for x, y in Data]
    X = [log(I) for I in N]

    pass
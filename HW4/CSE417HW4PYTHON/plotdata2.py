"""
Name: Hongdali
Class: Cse 417

This is a file that is used to plot that data created for HW4 problem 5, or 6.
"""

import matplotlib.pyplot as plt
import json as j


def main():
    with open("coloringdata.json") as f:
        jsonFile = j.load(f)
    print(jsonFile)
    X = []
    Y = []

    for smallerData in jsonFile:
        X.append(smallerData["p"])
        Y.append(smallerData["AvgColor"])
    print(f"X: {X}")
    print(F"Y: {Y}")
    plt.plot(X, Y)
    plt.xticks(fontsize=7)
    plt.title(f"Average Color used for random graphs where n = {smallerData['n']}")
    plt.xlabel("Edge Density")
    plt.ylabel("Average Number of Color Used")
    plt.savefig(f"Avgcolorusage")
    plt.clf()


if __name__ == "__main__":
    main()
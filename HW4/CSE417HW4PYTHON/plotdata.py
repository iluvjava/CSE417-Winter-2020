"""
Name: Hongda Li
Class: cse 417

This file is created to visualized data produced from the csharp program.
"""

import matplotlib.pyplot as plt
import json as j


def main():
    with open("data.json") as f:
        jsonFile = j.load(f)
    print(jsonFile)
    X = []
    Y = []
    for smallerData in jsonFile:
        for x, y in list(smallerData.items())[2:]:
            X.append(x)
            Y.append(y)
        plt.bar(X,Y)
        plt.savefig("plot")

if __name__ == "__main__":
    main()
    pass
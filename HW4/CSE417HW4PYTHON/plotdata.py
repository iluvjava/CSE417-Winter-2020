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
    for smallerData, I in zip(jsonFile, range(len(jsonFile))):
        for x, y in list(smallerData.items())[2:]:
            X.append(x)
            Y.append(y)

        plt.bar(X,Y, width=1)
        plt.xticks(fontsize=7)
        plt.title(f"Vertex Degree Distribution wit p = {smallerData['p']}; n = {smallerData['n']}")
        plt.savefig(f"plot{I}")

if __name__ == "__main__":
    main()
    pass
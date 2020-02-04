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

    for smallerData, I in zip(jsonFile, range(len(jsonFile))):
        X = []
        Y = []
        for k in list(smallerData.keys())[2:]:
            X.append(int(k))
            Y.append(smallerData[k])
        print(f"X: {X}")
        print(F"Y: {Y}")
        plt.bar(X, Y, width=1)
        plt.xticks(fontsize=7)
        plt.title(f"Vertex Degree Distribution wit p = {smallerData['p']}; n = {smallerData['n']}")
        plt.savefig(f"plot{I}")
        plt.clf()



if __name__ == "__main__":
    main()
    pass
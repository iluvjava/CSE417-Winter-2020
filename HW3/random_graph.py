"""
Name: Hongda Li
Class: cse 417

This file contains a method that craetes a random graph given the edge density and the number of
vertices involved.
"""

from random import random
r = random
def rand_g(n: int, p: int):
    """
        The graph is undirected, no self edges.
        It's represented as an adjacency list.
    :param n:
        Vertex count.
    :param p:
        Edge density.
    """
    assert n > 2 and p > 0 and p <= 1, "Invalid inputs"
    G = [[] for I in range(n)]
    for I in range(n):
        for J in range(I + 1, n):
            if r() <= p:
                G[I].append(J)
                G[J].append(I)
    return G

if __name__ == "__main__":
    print(rand_g(5, 1))
    print(rand_g(5, 0.5))
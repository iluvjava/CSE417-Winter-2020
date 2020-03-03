"""
HW8
Cse 417 winter

THis file is the for the HW8. Dynamic programming and exact subset sum.
"""

from typing import List

STATES= ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
         "District of Columbia","Florida",
"Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
         "Massachusetts",
"Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico",
"New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina",
         "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

ELECTORIAL_VOTES = [9, 3, 11, 6, 55, 9, 7, 3, 3, 29, 16, 4, 4, 20, 11, 6, 6, 8, 8, 4, 10, 11, 16, 10, 6, 10, 3, 5, 6,
                    4, 14, 5, 29, 15, 3, 18, 7, 7, 20, 4, 9, 3, 11,
                    38, 6, 3, 13, 12, 5, 10, 3]


def exact_subsetsum_count(S: List[int], K):
    """

    :param S:
        List of integers you want to choose the subset and sum it up.
    :param K:
        The target number you want to sum up to.
    :return:
        1. The total number of subsets that sums up exactly to K.
        2. The Optimal table for the number of subset
        3. The Optimal table for the element included table.
            * This array will contain solution that has the most states in it.
    """
    S.sort()
    Opt1 = [[0 for I in range(K + 1)] for J in range(len(S) + 1)] # A table of none
    Opt2 = [[0 for I in range(K + 1)] for J in range(len(S) + 1)]
    for I in range(1, len(S) + 1):
        for J in range(1, K + 1):
            Opt1[I][J] += bool(S[I - 1] == J) + Opt1[I - 1][J]
            if J - S[I - 1] >= 0:
                Opt1[I][J] += Opt1[I - 1][J - S[I - 1]]
            Opt2[I][J] += max(Opt2[I][J], Opt2[I][J - S[I - 1]] + 1)\
                if J + S[I - 1] >= 0  else Opt2[I - 1][J - S[I - 1]]
    return Opt1[-1][-1], Opt1, Opt2

def interp_objval(S: List[int], A: List[List[int]], Coord=None, Soln = None):
    """
        This function will extract one of the solution from the 2d table of objective values.
        * The array the function returns is a list of indices, where it got mapped
        to a subset in the original set.
        * It interpret the results recursively.
    :param A:
        The 2d table contains the objective values.
    :param S:
        The ordered set that we are interested in.
    :return:
        An instance of the subset
    """
    Coord = (len(A) - 1, len(A[0]) - 1) if Coord is None else Coord
    Soln = [] if Soln is None else Soln
    I, J = Coord
    if I == 0 or J == 0:
        return Soln
    CurrentObjective = A[I][J]
    x = S[I - 1]
    if x <= J:
        if CurrentObjective == A[I - 1][J - x] + 1:
            Soln.append(I - 1)
            return interp_objval(S, A, (I - 1, J - x), Soln)
    return interp_objval(S, A, (I - 1, J), Soln)



    # TODO: IMPLEMENT THIS SHIT


if __name__ == "__main__":
    print(exact_subsetsum_count([1, 1, 1, 1], 2)[0])
    print(exact_subsetsum_count([1]*100, 4)[0])
    print(exact_subsetsum_count([1]*1000, 40)[0])
    print(exact_subsetsum_count(ELECTORIAL_VOTES, 269)[0])

    print("Testing objective interpretation: ")
    S = [1,1,1,1]
    Res = exact_subsetsum_count(S, 2)
    print(Res[-1])
    print(interp_objval(S, Res[-1]))
    pass
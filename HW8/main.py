"""
HW8
Cse 417 winter
Name: Hongda Li

So in one episode of season 5 of the My Little Pony: Friendship is magic, Colorara reunited with Applejack, her
childhood best friend. However, she was not the same pony as what Applejack remembered.

go and watch it..... Ok, I digressed,

seriously, working out how many ways the votes can sum up to 269 is the most boring application I have ever seen.

Like, TBH, it's even more boring than giving back changes in banknotes to customers! In fact there is a lot of
intricacy of real world application of using Dynamic programming on banknotes problem.

Yo, do leetcode and watch cartoon and take CSE classes man, life is chill; you should do the same bro.

You hear me! Do leetcode!!!

The technical interview problems are so much math, and some of them are even straight out logic and IQ test.

I have to admit it's pretty stupid cause it's literally discrete optimizations and arcane knowledge of some
weird math theorems, but that is what it makes the industry fun I guess? or may be it's only for people who love
computers, cause real mathematicians would just shrug at these topics in computer science, they are like, WAY more
interested in 17 century's conjectures and shit like that.
"""

from typing import List

STATES= ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
         "District of Columbia","Florida",
"Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
         "Massachusetts",
"Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico",
"New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina",
         "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
         "Wisconsin", "Wyoming"]

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
            x = S[I - 1]
            Opt1[I][J] += bool(x == J) + Opt1[I - 1][J]
            if J - x >= 0:
                Opt1[I][J] += Opt1[I - 1][J - x]

            # This part is for optimal solution with maximum number of elements:
            # Opt2[I][J] += max(Opt2[I - 1][J], Opt2[I - 1][J - S[I - 1]] + 1, bool(J == S[I - 1]))\
            #     if S[I - 1] <= J  else Opt2[I - 1][J - S[I - 1]]
            if x <= J:
                MaxVal = Opt2[I - 1][J]
                MaxVal = max(Opt2[I - 1][J - x] + (0 if Opt2[I - 1][J - x] == 0 else 1), MaxVal)
                MaxVal = max(bool(x == J), MaxVal)
                Opt2[I][J] = MaxVal
            else:
                Opt2[I][J] = Opt2[I - 1][J]

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

def main():
    Results = exact_subsetsum_count(ELECTORIAL_VOTES, 269)
    print("The total number of subsets that can reach a votes of 269 to 269 is the results returned "
           "divided by 2. ")
    print(f"The subsetsum count is: {Results[0]//2}")
    print("Now, we are interested in the optimal solution that inolves the most number of states: ")
    print("Here is the list of states and their votes that sum up to a total of 269, we are ignoring the complement.")
    StatesVotesPair = [(S, V) for S, V in zip(STATES, ELECTORIAL_VOTES)]
    StatesVotesPair.sort(key=lambda x: x[1])
    ResultsInterpreted = interp_objval([V for S, V in StatesVotesPair], Results[-1])
    RunningSum = 0
    for Idx in ResultsInterpreted:
        print(f"{StatesVotesPair[Idx][0]}: {StatesVotesPair[Idx][1]}")
        RunningSum += StatesVotesPair[Idx][1]
    print("Ok... making sure the sum of all the votes is indeed 269...")
    print(RunningSum)

if __name__ == "__main__":
    def temp():
        print(exact_subsetsum_count([1, 1, 1, 1], 2)[0])
        print(exact_subsetsum_count([1]*100, 4)[0])
        print(exact_subsetsum_count([1]*1000, 40)[0])
        print(exact_subsetsum_count(ELECTORIAL_VOTES, 269)[0])

        print("Testing objective interpretation: ")
        S = [1,1,1,1]
        Res = exact_subsetsum_count(S, 2)
        print(Res[-1])
        print(interp_objval(S, Res[-1]))
    temp()
    print("------------------------------------------------------")
    main()
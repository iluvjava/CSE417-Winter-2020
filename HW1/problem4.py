"""
Name: Hongda Li
Class: cse 417 winter 2020

This is a homework assignment for cse 417 winter 2020, it's implementing the Gale-Shapley
algorithm

It needs python 3.6 or above to run.

"""

from typing import List

def produce_stable_match(M: List[List[int]], W: List[List[int]]):
    """
    Function will produce a list of tuple representing the stable matching between the set M, W.

    The proposing side is: M.
    :param: M
        A n by n matrix,
        the i th row denotes the preference list of m_i
    :param: W
        A n by n matrix,
        the W th row denotes the preference list of w_i
    :return:
    A list of tuple in the following format:
    [(m_1, W_1), (m_2, w_2)... (m_n, w_2)]
    """
    pass

def dict_convert(M: List[List[int]]):
    """
        This function takes in the preference matrix and convert the value into a dictionary making he look up of
        preference value constant.
    """
    pass
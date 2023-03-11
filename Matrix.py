"""
Python3 program to Print all possible paths from
top left to bottom right of  n*n matrix.

"""

from random import randint
from copy import copy
from datetime import datetime

__author__ = "Pouria Keshtidar"
_email__ = "pkeshtidar@gmail.com"


bestPath = [[], 1000000]


# define random Matrix
def matrix(q):
    """
    :param q:
    :return:
    """
    lis = []
    for _ in range(q):
        lis2 = []
        for _ in range(q):
            r = randint(0, 9)
            lis2.append(r)
        lis.append(lis2)
    for x in range(q):
        print(lis[x], "\r")
    return lis


# find all Path's
def findpaths(list1, n1):
    """

    :param list1:
    :param n1:
    """
    path = [0 for _ in range(2 * n1 - 1)]
    coords = [0 for _ in range(2 * n1 - 1)]
    findpathsTool(list1, n1, 0, 0, path, coords, 0)


def findpathsTool(lst1, n2, i, j, path, coords, index):
    """

    :param lst1:
    :param n2:
    :param i:
    :param j:
    :param path:
    :param coords:
    :param index:
    :return:
    """
    # if we reach the bottom of lst, we can only move right.

    if i == n2 - 1:
        for k in range(j, n2):
            path[index + k - j] = lst1[i][k]
            coords[index + k - j] = (i, k)
        # After this loop, one path is completed.
        # Add it to paths list and print.
        total = sum(path)
        if bestPath[1] > total:
            bestPath[1] = copy(total)
            bestPath[0] = copy(coords)
        print(path, '=', total)
        print(coords, '=', total)
        return
    # if we reach to the right most corner, we can only move down.
    if j == n2 - 1:
        for k in range(i, n2):
            path[index + k - i] = lst1[k][j]
            coords[index + k - j] = (i, k)
        # After this loop, one path is completed.
        # Add it to paths list and print.
        total = sum(path)
        if bestPath[1] > total:
            bestPath[1] = copy(total)
            bestPath[0] = copy(coords)
        print(path, '=', total)
        print(coords, '=', total)
        return

    # add current element to the path list
    path[index] = lst1[i][j]
    coords[index] = (i, j)
    # move right in x direction and call findpathsTool recursively
    findpathsTool(lst1, n2, i + 1, j, path, coords, index + 1)
    # move down in y direction and call findpathsTool recursively
    findpathsTool(lst1, n2, i, j + 1, path, coords, index + 1)


if __name__ == '__main__':
    n = int(input("matrix: [n x n] \nn: "))
    start = datetime.now()
    lst = matrix(n)
    print('-------All possible Path-------------')
    findpaths(lst, n)
    print('------One of the Best Path-----------')
    print(bestPath[0], "=", bestPath[1])
    print("time = ", datetime.now() - start)

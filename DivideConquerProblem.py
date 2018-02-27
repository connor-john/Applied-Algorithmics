# -*- coding: utf-8 -*-
"""
Created on Sun Sep 03 16:54:51 2017

@author: ctay270
"""

from bisect import bisect_left
MAXN = 100000


def initialise(nList):
    for i in range(1, 6):
        for j in range(10 ** (i - 1), 10 ** i):
            nList[j] = nList[j - 1]
            temp = (j - 10 ** (i - 1) + 1) * i
            for k in range(1, i):
                temp += (10 ** k - 10 ** (k - 1)) * k
            nList[j] += temp
    return nList


def solve(nList, n):
    pos = bisect_left(nList, n)
    count = n - nList[pos - 1]
    total = 0
    for j in range(1, pos + 1):
        temp_j = j
        nLen = len(str(temp_j))
        for k in reversed(range(nLen)):
            answer = temp_j / 10 ** k
            total += 1
            if (total == count):
                print(int(answer))
                return
            temp = 10 ** (k)
            temp_j %= temp
            

def main():
    nList = [0] * MAXN
    n = 0
    initialise(nList)
    numTest = int(input(""))
    for itertest in range(0, numTest):
        n = int(input(""))
        solve(nList, n)

main()

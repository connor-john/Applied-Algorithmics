# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 20:14:12 2017

@author: Connor
"""
import sys

def solve(prob):
    op = prob[1:len(prob):2]
    nu = prob[0:len(prob) + 1:2]
    n = len(nu)
    minm = [[0 for i in range(n)] for j in range(n)]  
    maxm = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        minm[i][i] = int(nu[i])   
        maxm[i][i] = int(nu[i])  	
    for x in range(1, n):   
        for i in range(n - x):
            j = i + x
            minm[i][j], maxm[i][j] = maxpl(i, j, op, minm, maxm)
    return maxm[0][n-1]

def maxpl(i, j, op, m, Mm):
    s = 99999
    l = -99999
    for k in range(i, j):
        q = opr(Mm[i][k], Mm[k + 1][j], op[k])
        w = opr(Mm[i][k], m[k + 1][j], op[k])
        e = opr(m[i][k], Mm[k + 1][j], op[k])
        r = opr(m[i][k], m[k + 1][j], op[k])
        s = min(s, q, w, e, r)
        l = max(l, q, w, e, r)
    return(s, l)

def opr(a, b, op):
    if op == '+':
        return a + b
    if op == '*':
        return a * b
    

def main():
    
	test = str(sys.stdin.readline())
	for i in range(int(test)):
		prob = input()
		probsp = prob.split()
		print((solve(probsp)))


main()
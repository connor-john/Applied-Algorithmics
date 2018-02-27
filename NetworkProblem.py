# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:15:20 2017

@author: Connor
"""
import networkx as nx
from networkx.algorithms.flow import shortest_augmenting_path

def main():
    poss = True
    while poss:
        lList = []
        testcases = int(input())
        if testcases == 0:
            poss = False
        ress = 0
        while ress < testcases:
            val = input()
            spl = val.split()
            lList.append(spl)
            ress +=1
        if len(lList) != 0:
            res = solve(lList)
            print(res)
            
            

def solve(testlist):
    G = nx.DiGraph()
    dict1 = {}
    a = 0
    while a < (len(testlist)):
        b = 0
        G.add_node(str(a))
        dict1[str(a)] = len(testlist[a])
        while b < len(testlist[a]):
                s = testlist[a][b]
                G.add_edge(str(a),s, capacity=1.0)
                b+=1 
        a += 1
    a = 0
    c = 0
    while a < (len(testlist)):
        b = a + 1
        while b < (len(testlist)):
            if dict1[str(a)] >= c and dict1[str(b)] >= c:
                res = shortest_augmenting_path(G, str(a), str(b), two_phase=True)
                flow =  res.graph['flow_value']   
                if flow > c:
                    c = int(flow)
            b += 1
        a+= 1
    return(c)

main()
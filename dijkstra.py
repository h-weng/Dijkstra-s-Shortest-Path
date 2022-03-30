"""
    Dijkstra's shortest Path Implementation
    =======================================
    This implementation is for adjacency matrices to find the shortest path to each vertex from index 0 in a graph
    
    Dijkstra's Algorithm:
    
        https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        https://algs4.cs.princeton.edu/lectures/keynote/44ShortestPaths-2x2.pdf
        https://www.cs.cmu.edu/~15451-s20/lectures/lec09-dp2.pdf
        
"""

import math
  
G = [[0, 0, 2, 3, 0, 0, 0],
     [0, 0, 1, 0, 0, 5, 0],
     [2, 4, 0, 3, 2, 0, 0],
     [1, 0, 1, 0, 0, 1, 0],
     [0, 0, 3, 0, 0, 0, 2],
     [0, 2, 0, 1, 0, 0, 1],
     [0, 0, 4, 0, 0, 4, 0]]

g = len(G)
U = [i for i in range(g)]
Q = [[i, math.inf] if i !=0 else [0, 0] for i in range(g)]

def visit(Q, U):
    r = -math.inf
    for i in range(g):
        if Q[i][0] in U:
            if r < 0:
                r = i
            elif Q[i][1] <= Q[r][1]:
                r = i
    return r

def dijkstra(Q, U):
    while U:
        r = visit(Q, U)
        for n in Q:
            p = n[0]
            if G[r][p] != 0 and Q[p][0] in U:
                d = Q[r][1] + G[r][p]
                if d < Q[p][1]:
                    Q[p][1] = d
            if r in U:
                U.remove(r)
    return Q
  
p = dijkstra(Q, U)
print(p)

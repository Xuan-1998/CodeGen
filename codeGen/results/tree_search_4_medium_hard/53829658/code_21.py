import sys
from itertools import permutations

def find_capital_and_min_reversed_edges():
    n = int(sys.stdin.readline())
    graph = {}
    for _ in range(n-1):
        si, ti = map(int, sys.stdin.readline().split())
        if si not in graph:
            graph[si] = []
        if ti not in graph:
            graph[ti] = []
        graph[si].append(ti)
    
    dp = [0] * (n+1)
    for i in range(1, n):
        for j in graph[i]:
            dp[i] = min(dp[i], 1 + dp[j])
    
    min_reversed_edges = sum(dp)
    
    capitals = []
    for perm in permutations(range(1, n)):
        capital_sum = 0
        for city in range(1, n):
            capital_sum += dp[city]
        capitals.append((capital_sum, perm))
    
    best_capital_index = min(capitals)[1][0]
    print(min_reversed_edges)
    print(*capitals[best_capital_index][1], sep=' ')

find_capital_and_min_reversed_edges()

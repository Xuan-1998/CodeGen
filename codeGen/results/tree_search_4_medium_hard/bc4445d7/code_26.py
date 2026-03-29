import sys
from collections import defaultdict

def read_input():
    T = int(input())
    res = []
    for _ in range(T):
        n = int(input())
        edges = [list(map(int, input().split())) for _ in range(n-1)]
        m = int(input())
        prime_factors = list(map(int, input().split()))
        res.append((n, edges, m, prime_factors))
    return res

def solve_case(case):
    n, edges, m, prime_factors = case
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Initialize the table with base cases
    for i in range(2, n+1):
        dp[i][i] = 1
    
    # Fill up the table using dynamic programming
    for u, v in edges:
        for k in range(u, v+1):
            dp[u][v] = min(dp[u][k] + (dp[k][v] if k < v else 0), 
                            dp[u][v-1] + ((1 << (v-1)) if m == prime_factors[0] else 0))
    
    # Calculate the maximum possible distribution index
    max_dist_index = sum((dp[i][j] * prime_factors[j-i-1]) for i in range(2, n) 
                         for j in range(i+1, n+1))
    
    return max_dist_index % (10**9 + 7)

T = read_input()
for case in T:
    print(solve_case(case))

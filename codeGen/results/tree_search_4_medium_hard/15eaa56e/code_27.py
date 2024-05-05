import sys
from math import inf

def solve(n, m, k, tasks):
    dp = {(r, c): -inf for r in range(1, n+1) for c in range(1, m+1)}
    
    for l, r in tasks:
        for c in range(1, m+1):
            max_val = 0
            for i in range(l-1, r):
                max_val = max(max_val, dp[(i, c)])
            dp[(r, c)] = max_val
            
    for l, r in tasks:
        if any(dp[(r, c)] != -inf for c in range(1, m+1)):
            return "Yes"
    return "No"

n, m, k = map(int, input().split())
tasks = [tuple(map(int, input().split())) for _ in range(k)]

print(solve(n, m, k, tasks))

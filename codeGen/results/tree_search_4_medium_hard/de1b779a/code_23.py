import sys

def solve():
    n, m, c0, d0 = map(int, input().split())
    dp = {(i, j): 0 for i in range(c0+1) for j in range(m+1)}
    
    for _ in range(m):
        ai, bi, ci, di = map(int, input().split())
        
        for i in range(c0, -1, -1):
            if i >= ci:
                dp[(i-ci, j-1)] = max(dp[(i-ci, j-1)] + di, dp[(i, j-1)])
    
    return dp[(n, m)]

print(solve())

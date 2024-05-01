from math import inf

def min_squares(n, m):
    dp = {(i, j): float('inf') for i in range(1, n+1) for j in range(1, m+1)}
    
    dp[(1, j)] = 1 for j in range(1, m+1))
    dp[(i, 1)] = 1 for i in range(1, n+1))

    for i in range(2, n+1):
        for j in range(2, m+1):
            for k in range(1, min(i, j)+1):
                dp[(i, j)] = min(dp[(i, j)], (i-k)*(j-k) // k**2 + dp.get((i-k, j-k), inf))
    return dp[(n, m)]

n, m = map(int, input().split())
print(min_squares(n, m))

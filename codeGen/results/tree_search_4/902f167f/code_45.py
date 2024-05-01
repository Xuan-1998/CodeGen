from math import inf

dp = {(i, j): inf for i in range(1, 14) for j in range(1, 14)}

def min_squares(n, m):
    if n == 1 or m == 1:
        return 0
    
    for k in range(min(n, m)**0.5+1):
        dp[(n, m)] = min(dp[(k, k)] + (n-k*k)*(m-k*k), dp[(n, m)])
    
    return dp[(n, m)]

n, m = map(int, input().split())
print(min_squares(n, m))

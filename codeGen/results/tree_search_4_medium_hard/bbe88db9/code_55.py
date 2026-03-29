p = [int(x) for x in input().split()]
n = len(p)
dp = [[0] * (n + 1) for _ in range(n + 1)]

def solve(i, j):
    if i > n:
        return 1
    if dp[i][j] > 0:
        return dp[i][j]
    if j < i:
        return 0
    
    if p[i - 1] == j and i % 2 == 1:
        return solve(i + 1, p[i])
    elif p[i - 1] == j and i % 2 == 0:
        return 1
    else:
        return min(solve(i + 1, j), solve(i + 1, p[i])) + (i % 2)

print(solve(1, n + 1) % 1000000007)

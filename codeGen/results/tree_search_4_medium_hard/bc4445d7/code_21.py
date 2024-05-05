import sys

# Read input
n = int(input())
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))
m = int(input())
prime_factors = list(map(int, input().split()))

# Initialize memoization array
dp = [[[[-1] * (n + 1)] * (n + 1)] * (10**6 + 7) for _ in range(n + 1)]

def memoize(i, j, k, l):
    if dp[i][j][k][l] != -1:
        return dp[i][j][k][l]
    if i == j:
        if k == 0 and l == 0:
            return 1
        else:
            return -1
    if l < len(str(k)):
        for p in prime_factors:
            if k % p == 0:
                new_k = k // p
                new_l = l + 1
                if memoize(i, j, new_k, new_l) != -1:
                    dp[i][j][k][l] = (dp[i][j][new_k][new_l] or 1)
                    return dp[i][j][k][l]
        for p in prime_factors:
            if k % (p * p) == 0 and l + 2 <= len(str(k)):
                new_k = k // (p * p)
                new_l = l + 2
                if memoize(i, j, new_k, new_l) != -1:
                    dp[i][j][k][l] = (dp[i][j][new_k][new_l] or 1)
                    return dp[i][j][k][l]
        for p in prime_factors:
            if k % (p * p * p) == 0 and l + 3 <= len(str(k)):
                new_k = k // (p * p * p)
                new_l = l + 3
                if memoize(i, j, new_k, new_l) != -1:
                    dp[i][j][k][l] = (dp[i][j][new_k][new_l] or 1)
                    return dp[i][j][k][l]
        dp[i][j][k][l] = -1
    return dp[i][j][k][l]

# Calculate maximum distribution index
max_index = 0
for u, v in edges:
    for k in range(10**6 + 7):
        if memoize(u, v, k, 0) != -1:
            max_index = max(max_index, k)

print(max_index % (10**9 + 7))

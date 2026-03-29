import sys

n = int(input())
dp = [[False] * (n-1) for _ in range(n+1)]
memo = {}

def can_reach(i, k):
    if i > n or k < 0:
        return False
    if memo.get((i, k)):
        return memo[(i, k)]

    if k == 0 and i == n:
        return True

    reached = False
    for j in range(1, n+1):
        if dp[j][k-1]:
            reached = True
            break

    memo[(i, k)] = reached
    return reached

capital_cities = [False] * (n+1)
min_edges = float('inf')
for i in range(1, n+1):
    for j in range(n-1):
        if can_reach(i, j+1) and not dp[i][j]:
            capital_cities[i] = True
            min_edges = min(min_edges, j+1)
            break

print(min_edges)
for i in range(1, n+1):
    if capital_cities[i]:
        print(*range(1, i+1), sep=' ')

from collections import deque

n, k = map(int, input().split())
s = input()

dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = [""] * (k+1)

memo = set()

def dfs(i, j):
    if (i, j) in memo:
        return dp[i][j]
    if i == 0 and j > 0:
        return [""] * (j+1)
    if i > 0 and j <= n:
        delete = dfs(i-1, j)
        keep = dfs(i-1, j-1) + [s[i-1]]
        dp[i][j] = min(delete, keep, key=lambda x: (''.join(x), len(x)))
        memo.add((i, j))
    return dp[i][j]

print(''.join(dfs(n, k)))

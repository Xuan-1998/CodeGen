===BEGIN CODE===
from collections import defaultdict
n = int(input())
p = list(map(int, input().split()))
dp = [[False] * (2 * n + 1) for _ in range(n + 1)]
memo = defaultdict(dict)

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def dfs(i, j):
    if i > n or j > 2 * n:
        return False
    if dp[i][j]:
        return True
    if memo[i].get(j, None) is not None:
        return memo[i][j]
    for k in range(1, min(i + 1, j + 1)):
        a = list(range(k))
        b = list(range(k, k + i)) + list(range(k + i, k + j))
        if all(x < y for x, y in zip(a, b)) and all(x > y for x, y in zip(b, a)):
            if merge(a, b) == p[:j]:
                dp[i][j] = True
                memo[i][j] = True
    memo[i][j] = any(dfs(i - 1, j - k) for k in range(1, min(i + 1, j + 1)))
    return dp[i][j]

for _ in range(n):
    i, j = map(int, input().split())
    if dfs(i, j):
        print("YES")
    else:
        print("NO")

===END CODE===

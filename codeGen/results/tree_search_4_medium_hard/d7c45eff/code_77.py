import sys
from collections import deque

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [['' for _ in range(k+1)] for _ in range(n+1)]
    seen = set()

    queue = deque([(n, k)])
    while queue:
        i, j = queue.popleft()
        if j == 0:
            continue
        if i < n and (dp[i-1][j-1] + s[i-1]) not in seen:
            dp[i][j] = min(dp[i][j], dp[i-1][j-1] + s[i-1])
            queue.append((i, j-1))
            seen.add(dp[i][j])
        if i > 0 and (dp[i-2][j-1] + s[i-1]) not in seen:
            dp[i][j] = min(dp[i][j], dp[i-2][j-1] + s[i-1])
            queue.append((i-1, j-1))
            seen.add(dp[i][j])

    return dp[n][k]

print(solve())

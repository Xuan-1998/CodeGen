def make_zero(arr):
    n = len(arr)
    dp = [[False] * 2 for _ in range(n + 1)]

    # Base case: entire array has an optimal solution
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(2):  # 0 or 1 (unchanged or changed)
            if j == 0:  # unchanged
                dp[i][j] = dp[i-1][j] and dp[n-i-1][0]
            else:  # changed
                dp[i][j] = dp[n-i-1][1-j]

    return "YES" if dp[n][0] else "NO"

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(make_zero(arr))

def min_operations(n, x):
    dp = [[i for _ in range(10**(n-1))] for i in range(n+1)]

    for i in range(2, n+1):
        for j in range(max(10**(i-1)-1, 1), min(10**i, 10**(n-1))+1):
            if len(str(j)) == i:
                dp[i][j] = 0
            else:
                dp[i][j] = 1 + min(dp[k][j//10] for k in range(i) if j//10 >= 10**(k-1))

    return dp[n-1][x]

import sys

n, x = map(int, input().split())
print(min_operations(n, x))

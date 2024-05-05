def minMultiplications(p):
    n = len(p)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(2, n+1):
        dp[i][i] = 0
        for j in range(i-1, -1, -1):
            dp[j][i] = float('inf')
            for k in range(j, i):
                q = p[k] * p[k+1]
                cost = dp[j][k] + dp[k+1][i] + log(q)
                if cost < dp[j][i]:
                    dp[j][i] = cost
    res = ""
    i, j = 0, n-1
    while i < j:
        for k in range(i, j):
            q = p[k] * p[k+1]
            if dp[i][k] + dp[k+1][j] == dp[i][j]:
                res += "("
                for l in range(i, k+1):
                    res += "A" + str(l) + ","
                res += ")(" + str(k+1) + " * A" + str(j) + ")"
                i = k+1
                break
    return res

import sys
input = sys.stdin.readline
n = int(input())
p = [int(x) for x in input().split()]
print(minMultiplications(p))

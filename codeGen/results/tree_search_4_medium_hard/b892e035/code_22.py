import sys

T = int(input())

for _ in range(T):
    n = int(input())
    probs = [list(map(int, input().split())) for _ in range(n)]
    
    dp = [0.0] * (n + 1)
    dp[1] = probs[0][0]
    
    for i in range(2, n + 1):
        dp[i] = 0
        for j in range(i):
            if probs[i - 1][0] != probs[j][1] and probs[i - 1][0] != probs[j][2]:
                dp[i] += dp[j] * (probs[i - 1][0] / 100) * ((100 - probs[i - 1][0]) / 99)
        print("{:.6f}".format(dp[n]))

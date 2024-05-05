from sys import stdin

def solve():
    n = int(stdin.readline())
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        consecutiveOnesCount = 0
        for j in range(i - 1, -1, -1):
            if (j & 1) == 1 and ((j >> 1) & 1) == 1:
                consecutiveOnesCount += 1
            else:
                dp[i] += 1
        if consecutiveOnesCount > 0:
            dp[i] -= consecutiveOnesCount
    print(dp[n])

solve()

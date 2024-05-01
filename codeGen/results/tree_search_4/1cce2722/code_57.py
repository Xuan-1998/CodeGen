def maxPoints(a):
    n = len(a)
    dp = [[0]*(n) for _ in range(n)]

    for i in range(1, n):
        for k in range(min(i+1, a[i])):
            if k == 0:
                dp[i][k] = dp[i-1][k]
            else:
                dp[i][k] = max(dp[i-1][k], dp[max(0, i-k*2)][min(k, i-k*2)])

    return dp[-1][0]

# Read the input
n = int(input())
a = list(map(int, input().split()))

print(maxPoints(a))

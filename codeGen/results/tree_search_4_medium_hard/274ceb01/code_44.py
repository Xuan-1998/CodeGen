===BEGIN CODE===
def solve():
    n = int(input())
    marks = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(i):
            if k > 0:
                dp[i][k] = min(dp[k-1][0], dp[k-1][k]) + (i-k)*k
            else:
                dp[i][k] = i

    return dp[-1][-1]

print(solve())
===END CODE===

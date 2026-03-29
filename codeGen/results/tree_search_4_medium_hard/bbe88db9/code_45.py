def solution():
    n = int(input())
    p = list(map(int, input().split()))
    dp = [0] * (n + 2)
    dp[1] = 1

    for i in range(2, n + 1):
        if i % 2 == 0:
            dp[i] = (dp[p[i - 1]] + dp[i // 2]) % (10**9 + 7)
        else:
            dp[i] = (dp[p[i - 1]] + dp[(i - 1) // 2]) % (10**9 + 7)

    return dp[n + 1]

print(solution())

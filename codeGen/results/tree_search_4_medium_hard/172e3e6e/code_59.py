import sys

def good_subsequences():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [[0] * (10**6 + 7) for _ in range(n + 1)]

    dp[0][1] = 1

    for i in range(1, n + 1):
        for max_divisor in range(2, a[i] + 1):
            if a[i] % max_divisor == 0:
                dp[i][max_divisor] = (dp[i-1][max_divisor] * (i - 1) + (a[i] == 1)) % (10**9 + 7)
            else:
                dp[i][max_divisor] = 0

    answer = sum(dp[n][max_divisor] for max_divisor in range(2, a[n] + 1))
    print(answer)

good_subsequences()

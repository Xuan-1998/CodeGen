import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i):
            if i - j <= 9:   # edge case: when A and B have the same number of digits
                dp[i] += dp[j]
            else:
                dp[i] += dp[j] * (10 ** (i - j) - 1)
    print(dp[-1] / (2 ** N))  # normalize by total number of pairs

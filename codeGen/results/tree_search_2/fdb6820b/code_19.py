import sys

def solve(m, N, array):
    dp = [0] * (N + 1)
    dp[0] = 1
    for k in array:
        for i in range(k, N + 1):
            dp[i] += dp[i - k]
    return sum(1 if i <= N else 0 for i in dp) % (10**9 + 7)

m, N = map(int, input().split())
array = list(map(int, input().split()))
print(solve(m, N, array))

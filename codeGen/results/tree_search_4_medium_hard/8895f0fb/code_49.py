import sys

def expected_carries(N):
    dp = [0] * (N + 1)
    dp[0] = 0.5  # base case: adding two single-digit numbers
    for i in range(1, N + 1):
        for j in range(i):
            k = i - j
            if j > 0 and k > 0:
                dp[i] += dp[j] * dp[k]
            else:
                dp[i] = (dp[j] or dp[k]) / 2
    return sum(dp[1:]) / ((N ** 2) + N) // 2

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(expected_carries(N))

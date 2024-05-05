import sys

def solve(n, m, a, b):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: when n = 1 and prev_operations = 0
    dp[1][0] = 0

    for i in range(2, n + 1):
        for j in range(min(i, m)):
            if i % 2 == 1:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + a[i]
            else:
                p = b[j]
                if is_good_prime(p):
                    dp[i][j] = max(dp[i // 2][j - 1], dp[i // 2][j - 1] - a[i])
                else:
                    dp[i][j] = max(dp[i // 2][j - 1], dp[i // 2][j - 1] + a[i])

    return dp[n][0]

def is_good_prime(p):
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

print(solve(n, m, a, b))

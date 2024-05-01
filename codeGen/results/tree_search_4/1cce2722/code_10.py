import sys

def max_points(a):
    n = len(a)
    k = max(a)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i % k == 0:
            dp[i] = dp[i - 1]
        else:
            dp[i] = max(dp[i - 1], dp[i - 2] + 1) if i > 1 and a[i - 1] % k != a[i - 2] % k else 0

    return dp[n]

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]
print(max_points(a))

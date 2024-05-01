def maxPoints(a):
    n = len(a)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if a[i - 1] == a[0]:
            dp[i] = dp[i - 1]
        else:
            dp[i] = max(dp[i - 1], i)
            for k in range(i):
                if abs(a[i - 1] - a[k]) > abs(a[0] - a[k]):
                    dp[i] = max(dp[i], dp[k] + (k - i) + (n - k))

    return n - dp[-1]

# Read input
n = int(input())
a = list(map(int, input().split()))

print(maxPoints(a))

def max_points(a):
    n = len(a)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        elif a[i] == a[i-1] + 1 or a[i] == a[i-1] - 1:
            dp[i] = max(dp[i-1], 2)
        else:
            dp[i] = dp[i-1]

    return dp[-1]

# Read input from stdin
n = int(input())
a = list(map(int, input().split()))

print(max_points(a))

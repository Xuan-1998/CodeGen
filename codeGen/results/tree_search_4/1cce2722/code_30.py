def max_points(a):
    n = len(a)
    dp = [-float('inf')] * (n + 1)

    dp[0] = 0

    for i in range(1, n + 1):
        k = i - 1
        while k >= 0 and a[k] != a[i]:
            k -= 1
        dp[i] = max(dp[i-1], dp[k+1] if k >= 0 else 0) if k >= 0 else 0

    return dp[-1]

n = int(input())
a = list(map(int, input().split()))
print(max_points(a))

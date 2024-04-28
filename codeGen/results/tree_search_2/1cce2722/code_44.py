def max_points(a):
    n = len(a)
    dp = [n] * (n + 1)  # Initialize dynamic programming array

    for i in range(2, n):
        k = a[i]
        min_points = float('inf')
        for j in range(max(0, k - 2), min(n, k + 2)):
            if a[j] <= k:
                min_points = min(min_points, dp[j])
        dp[i] = 1 + min_points

    return dp[-1]

a = list(map(int, input().split()))
print(max_points(a))

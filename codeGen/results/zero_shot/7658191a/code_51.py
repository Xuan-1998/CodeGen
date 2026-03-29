def max_score(arr, k, z):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i <= k:
            dp[i] = max(dp[i - 1], arr[i - 1])
        else:
            for j in range(min(i, z), 0, -1):
                dp[i] = max(dp[i], dp[i - j] + arr[i - j])

    return dp[n]

# Example usage
t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(arr, k, z))

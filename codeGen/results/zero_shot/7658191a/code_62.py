def max_score(arr, k, z):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
        else:
            dp[i] = dp[i - 1]

    return min(max(dp[n - 1]), k)

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min(max(score(arr, k, z)), k))

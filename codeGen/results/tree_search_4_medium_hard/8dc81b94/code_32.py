def can_zero_all(arr):
    n = len(arr)
    max_val = max(arr)

    dp = [[False] * (max_val + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for k in range(max_val + 1):
            if arr[i - 1] > k:
                dp[i][k] = (dp[i - 1][max(0, min(arr[i - 1], k))] and arr[i - 1] > 0)
            else:
                dp[i][k] = (dp[i - 1][min(max(0, k - arr[i - 1]), 10**6)] and arr[i - 1] < k)

    return "YES" if dp[n][0] else "NO"

# Read input from stdin
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_zero_all(arr))

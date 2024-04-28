def max_partitions(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if prefix_sum[i - 1] == prefix_sum[n] - prefix_sum[i]:
            dp[i] = max(dp[i - 1], 1)
        else:
            dp[i] = max(dp[i - 1], 0)

    return max(dp)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))

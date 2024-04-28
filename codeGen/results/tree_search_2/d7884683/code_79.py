def max_partitions(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    dp = [0] * n
    left_sum = prefix_sum[0]
    right_sum = prefix_sum[-1]
    for i in range(1, n - 1):
        if left_sum == right_sum:
            dp[i] = 1
        else:
            left_sum += arr[i - 1]
            right_sum -= arr[n - i - 2]
            if left_sum == right_sum:
                dp[i] = 1

    max_partitions = 0
    for i in range(1, n):
        max_partitions = max(max_partitions, dp[i - 1])

    return max_partitions + 1


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))

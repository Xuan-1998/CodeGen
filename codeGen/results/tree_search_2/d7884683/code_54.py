def max_partitions(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    dp = [[0, 0]] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if prefix_sum[i] - prefix_sum[j] == 0:
                dp[i][1] = max(dp[i][1], dp[j][1] + 1)

    return max(map(lambda x: x[1], dp))

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))

def max_partitions(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        sum_left = 0
        for j in range(i):
            sum_left += arr[j]
            if sum_left == sum(arr[j:i]):
                dp[i] = max(dp[i], dp[j] + 1)

    return dp[-1]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))

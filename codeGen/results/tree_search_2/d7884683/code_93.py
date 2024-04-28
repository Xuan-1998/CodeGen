def max_partitions(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(n, -1, -1):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])
        if left_sum == right_sum:
            dp[i] = max(dp[:i]) + 1
        else:
            dp[i] = max(dp[:i])

    return dp[0]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))

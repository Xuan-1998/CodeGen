def partition_count(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        left_sum = sum(arr[:i])
        right_sum = -sum(arr[i:])
        if i % 2 == 1:
            dp[i] = max(dp[i-1], 1 + dp[(i+1)//2-1] if left_sum == right_sum else 0)
        else:
            dp[i] = max(dp[i-1], 1 + dp[i//2-1] if left_sum == -right_sum else 0)

    return dp[-1]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(partition_count(arr))

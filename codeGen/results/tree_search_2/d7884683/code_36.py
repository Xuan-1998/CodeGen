def partition_times(arr):
    n = len(arr)
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    total_sum = sum(arr)

    for i in range(1, n + 1):
        left_sum = 0
        for j in range(i, -1, -1):
            left_sum += arr[j]
            if left_sum == (total_sum - left_sum) // 2:
                dp[i][j] = max(dp[i-1][j-1], 1 + (dp[j-1][i-1] if j < i else 0))
    
    return dp[n][n]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(partition_times(arr))


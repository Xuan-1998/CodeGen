def min_operations(arr):
    n = len(arr)
    dp = [0] * n

    for i in range(1, n):
        dp[i] = float('inf')
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = min(dp[i], 1 + dp[j])
    return dp[-1]

n = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))

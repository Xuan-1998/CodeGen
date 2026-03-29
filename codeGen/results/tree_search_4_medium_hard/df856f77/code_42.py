def min_operations(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i == 1:
            dp[i] = arr[0]
        else:
            dp[i] = min(dp[i-1] + (arr[i] - arr[i-1]), dp[0] + i)
    
    return dp[-1]

n = int(input())
arr = list(map(int, input().split()))
print(min_operations(arr))

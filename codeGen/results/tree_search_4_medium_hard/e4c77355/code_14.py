def LIS(arr):
    n = len(arr)
    dp = [1] * n
    
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Read input from stdin
arr = [int(x) for x in input().split()]

print(LIS(arr))

def findDivisibleSubset(n, arr, m):
    # Sort the array first to avoid unnecessary checks
    arr.sort()
    
    dp = [False] * (m+1)
    dp[0] = True
    
    for i in range(1, n+1):
        for j in range(m, -1, -1):
            if j >= arr[i-1]:
                dp[j] = dp[j] or dp[j-arr[i-1]]
    
    return 1 if any(dp[m]) else 0

n = int(input())
m = int(input())
arr = list(map(int, input().split()))
print(findDivisibleSubset(n, arr, m))

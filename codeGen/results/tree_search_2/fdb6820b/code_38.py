import sys

def count_ways(arr, N):
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for i in range(1, N + 1):
        for num in arr:
            if i >= num:
                dp[i] += dp[i - num]
    
    return dp[N] % (10**9 + 7)

m, N = map(int, input().split())
arr = list(map(int, input().split()))
print(count_ways(arr, N))

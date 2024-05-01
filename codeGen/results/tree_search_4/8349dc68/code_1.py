import sys

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i <= k:
            dp[i] = min(arr[:i])
        else:
            dp[i] = max(dp[i-1], arr[i-k:i].count(min(arr[i-k:i])) * min(arr[i-k:i]))
    
    return dp[-1]

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(maxSumAfterPartitioning(arr, k))

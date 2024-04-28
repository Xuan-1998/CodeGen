import sys

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(n - k + 1):
        window_sum = sum(arr[i:i+k])
        dp[i+k] = max(dp[i] + window_sum, arr[i+k-1])
        
    return dp[-1]

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    print(maxSumAfterPartitioning(arr, k))

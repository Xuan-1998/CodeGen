from collections import defaultdict

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    
    # Initialize dp table with zeros
    dp = [[0] * (k + 1) for _ in range(n)]
    
    memo = defaultdict(int)
    
    for i in range(k, n):
        j = min(i, k)
        if i - j >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-j][j] + sum(arr[i-j:i]))
        else:
            dp[i][j] = sum(arr[:i+1])
    
    return max(sum(arr[i:i+k]) for i in range(n-k))

k, n = map(int, input().split())
arr = list(map(int, input().split()))
print(max_sum_after_partitioning(arr, k))

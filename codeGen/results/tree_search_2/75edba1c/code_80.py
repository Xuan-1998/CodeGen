def count_subarrays(Arr, K):
    n = len(Arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_val = max(Arr[i - 1:i + 1])
        
        if max_val > K:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    
    return dp[-1]

if __name__ == "__main__":
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))
    
    print(count_subarrays(Arr, K))

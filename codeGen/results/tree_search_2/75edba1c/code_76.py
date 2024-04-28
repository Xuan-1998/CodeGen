def count_subarrays(Arr, K):
    n = len(Arr)
    dp = [0] * (n + 1)

    max_val = -float('inf')
    left = 0
    right = 0

    while right < n:
        max_val = max(max_val, Arr[right])
        
        if max_val > K:
            dp[right + 1] = dp[right] + 1 if left == 0 else dp[left]
        else:
            left += 1
        
        right += 1
    
    return sum(dp) - (dp[-2] if n > 0 else 0)

N, K = map(int, input().split())
Arr = list(map(int, input().split()))
print(count_subarrays(Arr, K))

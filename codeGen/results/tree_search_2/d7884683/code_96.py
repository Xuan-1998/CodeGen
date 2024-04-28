from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    left_sum = sum(arr[:1])
    right_sum = sum(arr[1:])
    
    for i in range(2, n+1):
        if left_sum == right_sum:
            dp[i] = dp[i-1] + 1
        else:
            left_sum -= arr[i-1]
            right_sum += arr[i-1]
        
        if left_sum == right_sum and left_sum != sum(arr[:i]):
            dp[i] = max(dp[i], dp[i-1] + 1)
    
    print(max(dp))

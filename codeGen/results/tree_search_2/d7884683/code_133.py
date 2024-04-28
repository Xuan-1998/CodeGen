import sys

def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        dp = [0] * (n + 1)
        
        total_sum = sum(arr)
        left_sum = 0
        
        for i in range(n):
            left_sum += arr[i]
            
            if left_sum == total_sum - left_sum:
                dp[i + 1] = dp[i] + 1
            else:
                dp[i + 1] = max(dp[i], (i // 2) + (dp[i // 2] if i % 2 == 0 and sum(arr[:i // 2 + 1]) == total_sum - left_sum else 0))
        
        print(dp[-1])

solve()

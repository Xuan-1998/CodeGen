import sys

def min_possible_value():
    t = int(input())
    
    for _ in range(t):
        n, s = map(int, input().split())
        
        a = list(map(int, input().split()))
        dp = [0] + [sys.maxsize] * n
        
        for i in range(n):
            for j in range(i+1):
                dp[i+1] = min(dp[i+1], dp[j] + (a[i] - s) * (s if i == 0 else a[i-1]))
        
        print(dp[-1])

min_possible_value()

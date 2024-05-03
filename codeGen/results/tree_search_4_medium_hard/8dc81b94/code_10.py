import sys

def solve():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    dp = [0] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        dp[i] = float('inf')
        
        # Consider decrementing from the beginning
        if i > 0:
            dp[i] = min(dp[i], dp[i - 1] + abs(arr[i - 1]))
        
        # Consider decrementing from the end
        if i < n:
            dp[i] = min(dp[i], dp[i + 1] + abs(arr[i]))
    
    result = "YES" if dp[-1] != float('inf') else "NO"
    
    print(result)

solve()

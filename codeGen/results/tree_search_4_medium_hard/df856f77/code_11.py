from sys import stdin

def min_operations():
    n = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    
    dp = [0] * (n + 1)
    
    for i in range(1, n):
        dp[i] = float('inf')
        for k in range(i):
            dp[i] = min(dp[i], dp[k] + abs(A[i] - A[k]))
    
    return dp[-1]

print(min_operations())

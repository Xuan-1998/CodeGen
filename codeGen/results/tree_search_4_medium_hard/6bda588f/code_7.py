import sys

def min_value(s):
    dp = [[0] * (2*s + 1) for _ in range(n+1)]
    
    # Calculate the minimum value for F when i = 1.
    for j in range(2*s + 1):
        if j <= s:
            dp[1][j] = a1
        else:
            dp[1][j] = -a1
            
    # Use dynamic programming to calculate the minimum value for F.
    for i in range(2, n+1):
        for j in range(2*s + 1):
            if j <= s:
                dp[i][j] = min(dp[i-1][k] - a1 for k in range(j+1))
            else:
                dp[i][j] = min(dp[i-1][k] + a1 for k in range(j+1))
                
    # Calculate the minimum value for F.
    return min(dp[n])

t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_value(s))


# BEGIN SOLUTION
import sys

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    mod = 10**9 + 7
    
    dp = [[0] * (m+1) for _ in range(11)]
    
    # Base case: length of the resulting number after no operations
    for i in range(1, 11):
        dp[i][0] = i
        
    for j in range(1, m+1):
        for i in range(10, 0, -1):
            if i > 1:
                dp[i][j] = (dp[i-1][j-1] + 1) % mod
            else:
                dp[i][j] = 1
    
    # Calculate the length of the resulting number after m operations on a number with n digits
    result = (dp[n//10 if n >= 10 else 0][m]) % mod
    print(result)
# END SOLUTION

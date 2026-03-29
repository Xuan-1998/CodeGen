def min_operations(n, x):
    dp = [[float('inf')] * (10**n) for _ in range(n+1)]
    
    # Base cases
    for i in range(1, n+1):
        dp[i][0] = 0
    
    for _ in range(n+1):
        for x_val in range(1, 10**n):
            if len(str(x_val)) == n:
                dp[1][x_val] = 0
            else:
                min_ops = float('inf')
                for digit in str(x_val)[::-1]:
                    new_x = int(digit + str(x_val)[len(str(x_val))-1:])
                    min_ops = min(min_ops, dp[1][new_x])
                dp[1][x_val] = 1 + min_ops
    
    for i in range(2, n+1):
        for x_val in range(1, 10**n):
            if len(str(x_val)) == i:
                dp[i][x_val] = 0
            else:
                min_ops = float('inf')
                new_x = int(str(x_val)[0])
                for digit in str(x_val)[1:]:
                    new_x *= int(digit)
                    min_ops = min(min_ops, dp[i-1][new_x])
                dp[i][x_val] = 1 + min_ops
    
    if x < 10**n:
        return -1
    else:
        return dp[n][x]

import sys

while True:
    n, x = map(int, input().split())
    print(min_operations(n, x))

import sys

def num_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        j = 1
        while j ** 2 <= i:
            if i - j ** 2 >= 0 and dp[i - j ** 2] != float('inf'):
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
            j += 1
    
    return dp[n]

n = int(input())
print(num_squares(n))

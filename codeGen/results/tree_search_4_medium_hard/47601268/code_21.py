import sys

def count_non_consecutive_ones(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    prev_bit = -1
    for i in range(1, n + 1):
        curr_bit = i & 1
        if curr_bit != prev_bit:
            dp[i] = 2 * dp[i - 1]
        else:
            dp[i] = dp[i - 1]
        prev_bit = curr_bit
    
    return dp[n]

n = int(input())
print(count_non_consecutive_ones(n))

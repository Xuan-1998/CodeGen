import sys
from collections import defaultdict

def max_bitwise_or(n, s):
    dp = [0] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if j == i - 1:
                bitwise_or = int(s[j:i+1], 2)
            else:
                bitwise_or = dp[j-1] | ((1 << (i-j)) - 1)
            dp[i] = max(dp[i], bitwise_or)

    return bin(dp[-1])[2:]

n = int(input())
s = input()
print(max_bitwise_or(n, s))

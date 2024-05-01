import sys
from collections import deque

def solve(n, s):
    dp = [0] * (1 << n)
    for mask in range(1, 1 << n):
        if s[0] == '1':
            dp[mask] += dp[mask ^ 1]
        else:
            for i in range(n):
                if (mask >> i) & 1:
                    break
            dp[mask] = 1
    return sorted([i for i in range(1 << n) if dp[i]])

n = int(input())
s = input()
print('\n'.join(map(str, solve(n, s))))

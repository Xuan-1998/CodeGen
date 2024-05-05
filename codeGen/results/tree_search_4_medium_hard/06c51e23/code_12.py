import sys
from math import floor, ceil

input = sys.stdin.readline

n, t = map(int, input().split())
fraction = float(input())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    
    for j in range(i):
        grade = floor(fraction * 10 ** j) / 10 ** j
        if t > 0:
            t -= 1
        else:
            break
        
        dp[i] = max(dp[i], dp[j] + grade)
        
    if t <= 0:
        break
    
print(int(ceil(dp[-1])))

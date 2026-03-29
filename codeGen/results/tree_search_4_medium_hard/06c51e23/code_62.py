code = '''
import sys

n, t = map(int, input().split())
fractional_part = [int(x) for x in input().split('.')[1:]]

dp = [0] * (n + 1)
dp_memo = [float('-inf')] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(dp[i-1], fractional_part[i-1])
    dp_memo[i] = fractional_part[i-1]
    if t >= i:
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + round(fractional_part[i-j-1]) - round(fractional_part[i-j-2]))

print(int(dp[-1]))
'''

print(code)

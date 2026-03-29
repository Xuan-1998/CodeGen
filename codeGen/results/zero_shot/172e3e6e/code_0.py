import sys
from collections import defaultdict

def read_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

n, a = read_input()

dp = [0] * (10**6 + 1)
dp[1] = len([x for x in a if x % 1 == 0])
for i in range(2, 10**6 + 1):
    dp[i] = dp[i - 1]
    for j in range(i):
        if i % (j + 1) == 0:
            dp[i] += dp[j]

print(dp[6] % (10**9 + 7))

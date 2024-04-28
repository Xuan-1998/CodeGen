from itertools import groupby
import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (n + 1)
max_sum = -sys.maxsize

for i in range(n):
    for j in range(i, min(i + k + 1, n)):
        dp[j + 1] = max(dp[j], sum(arr[i:j+1]))

print(max(dp))

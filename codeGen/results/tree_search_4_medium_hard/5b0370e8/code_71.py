import sys

input()
n, k = map(int, input().split())
print(sum([dp[2**k-1][i] for i in range(2**k)]))

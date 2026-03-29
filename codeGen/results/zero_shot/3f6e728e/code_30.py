from collections import Counter
import sys

input()
N, M, C = map(int, input().split())
upper_hemispheres = list(map(int, input().split()))
lower_hemispheres = list(map(int, input().split()))

total_radii = upper_hemispheres + lower_hemispheres
unique_radii = Counter(total_radii).keys()

dp = [0] * (C+1)
dp[0] = 1

for radius in unique_radii:
    for i in range(C, radius - 1, -1):
        dp[i] = (dp[i] + dp[i-radius]) % (10**9 + 7)

print(*dp[1:], sep=' ')

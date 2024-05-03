import sys

n, m = map(int, input().split())
dp = [0] * n
prev_species = 0

for _ in range(n):
    species = int(input()) - 1
    if species != prev_species:
        dp[_] = min(dp[_] + 1, _)
    else:
        dp[_] = _
    prev_species = species

print(min(dp))

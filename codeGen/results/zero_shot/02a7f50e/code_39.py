import sys

n = int(sys.stdin.readline())
positions = []
power_levels = []

for _ in range(n):
    position, power_level = map(int, sys.stdin.readline().split())
    positions.append(position)
    power_levels.append(power_level)

positions.sort()

dp = [0] * (len(positions) + 1)

for i in range(1, len(positions)):
    for j in range(i):
        if power_levels[i] > power_levels[j]:
            dp[i] = min(dp[i], dp[j] + 1)

print(min(dp))

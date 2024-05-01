import sys
from collections import defaultdict

def max_points_earned(n, sequence):
    dp = defaultdict(int)
    dp[0] = 0

    for i in range(1, n+1):
        max_points = 0
        for j in range(i-2, -1, -1):
            if (sequence[i-1] != sequence[j] + 1 and sequence[i-1] != sequence[j] - 1) or j == 0:
                max_points = max(max_points, dp[j] + i - j)
        dp[i] = max_points

    return dp[n]

n = int(input())
sequence = list(map(int, input().split()))
print(max_points_earned(n, sequence))

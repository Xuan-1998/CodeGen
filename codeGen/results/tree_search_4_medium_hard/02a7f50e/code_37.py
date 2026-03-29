import sys

def min_destroyed_beacons():
    n = int(input())
    dp = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        a, b = map(int, input().split())
        for j in reversed(range(i+1)):
            if j == 0:
                dp[i][j] = 0
            else:
                destroy_if_activated = min(destroyed + 1 for destroyed in range(b+1)) if i >= a and a - j <= b else float('inf')
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + (destroy_if_activated == float('inf') or destroy_if_activated))
        print(dp[-1][-1])

min_destroyed_beacons()

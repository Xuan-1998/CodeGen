import sys

def min_beacons_destroyed():
    n = int(input())
    beacons = []
    for _ in range(n):
        a, b = map(int, input().split())
        beacons.append((a, b))

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if all(a_j <= a_i for (_, a_i), (_, b_i) in beacons[:i]):
                dp[i][j] = min(dp[i-1][k-1] + 1 for k in range(j+1)) or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return min(dp[n])

print(min_beacons_destroyed())

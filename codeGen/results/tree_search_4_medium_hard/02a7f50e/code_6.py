def min_destroyed_beacons(n):
    beacons = []
    for _ in range(n):
        position, power = map(int, input().split())
        beacons.append((position, power))

    # Sort beacons by position (from right to left)
    beacons.sort(reverse=True)

    dp = [[0] * (1000001) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, 1000001):
            if j > beacons[i-1][1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][max(0, j-beacons[i-1][1]+1)]) + 1

    return dp[n][0]

n = int(input())
print(min_destroyed_beacons(n))

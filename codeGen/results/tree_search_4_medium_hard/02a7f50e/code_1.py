def minBeaconsDestroyed():
    n = int(input())  # Read the number of beacons from input
    positions = []  # Store the positions and power levels of the beacons
    for _ in range(n):
        a, b = map(int, input().split())
        positions.append((a, b))

    dp = [[0] * (10**6 + 1) for _ in range(100001)]
    for i in range(100000, -1, -1):
        for j in range(10**6 + 1):
            if j > 0:
                for k in range(i-1, -1, -1):
                    l = abs(i-k)
                    dp[i][j] = min(dp[i][j], dp[k][l] + 1)

    return min(dp[0][b] for a, b in positions)  # Return the minimum number of beacons destroyed

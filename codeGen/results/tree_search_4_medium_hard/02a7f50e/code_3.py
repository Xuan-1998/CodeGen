def min_beacons_destroyed():
    n = int(input())
    beacons = []
    for _ in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))

    dp = [[0] * (max(y) + 1) for _ in range(2)]
    dp[1] = [y for _, y in beacons]

    for i in range(n-2, -1, -1):
        for j in range(max(dp[1])):
            if j < dp[1][i]:
                dp[0][j] = min(dp[0][j], dp[1][i] - j)
            else:
                dp[0][j] = min(dp[0][j], 1 + dp[0][j-1])

    return sum(dp[0])

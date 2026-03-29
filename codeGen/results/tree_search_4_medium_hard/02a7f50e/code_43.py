from collections import defaultdict

def min_destroyed_beacons():
    n = int(input())
    beacons = [(int(a), int(b)) for _ in range(n)]
    beacons.sort()

    memo = defaultdict(int)
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    dp[0][0] = 0

    for i, (a, b) in enumerate(beacons):
        for j in range(i, -1, -1):
            k = min(j + 1, n)
            while k > j:
                if b >= beacons[k-1][0]:
                    dp[i+1][j] = min(dp[i+1][j], dp[j][k-1] + 1)
                k -= 1

    return dp[n][-1]

print(min_destroyed_beacons())

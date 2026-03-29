def min_beacons_destroyed(filename):
    n = int(input())  # number of beacons
    beacons = []  # list of beacons (position, power level)
    
    for _ in range(n):
        a, b = map(int, input().split())
        beacons.append((a, b))
    
    dp = [[float('inf')] * 1000001 for _ in range(100001)]
    dp[0][0] = 0
    
    for i, (a, b) in enumerate(beacons):
        for j in range(max(a, b), -1, -1):
            for k in range(i):
                if a > beacons[k][0]:
                    break
                if j - beacons[k][1] > 0:
                    dp[i][j] = min(dp[i][j], dp[k][min(j, beacons[k][1])] + (i-k))
    
    return min(dp[-1])

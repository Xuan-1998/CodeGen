def min_destroyed_beacons(n):
    dp = [[0] * 1000001 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, 1000001):
            if j <= b[i - 1]:
                dp[i][j] = dp[i - 1][max(0, j - b[i - 1])] + 1
            else:
                dp[i][j] = dp[i - 1][j]
    
    return min(dp[n])

n = int(input())
b = [int(input()) for _ in range(n)]
print(min_destroyed_beacons(n))

def solve():
    n = int(input())
    beacons = []
    for _ in range(n):
        a, b = map(int, input().split())
        beacons.append((a, b))

    dp = [[0] * 1000001 for _ in range(101)]
    for i in range(1, n+1):
        a_i, b_i = beacons[i-1]
        for j in range(1, b_i+1):
            if i > 0:
                dp[i][j] = min(dp[i-1][max(0, j-b_i)] + 1, sum([dp[k-1][min(k-1, j-b_i)] + 1 for k in range(1, i) if a_k <= a_i]))
            else:
                dp[i][j] = j

    print(min(dp[-1]))

if __name__ == "__main__":
    solve()

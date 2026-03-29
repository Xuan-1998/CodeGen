n, k, z = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[[0] * 2 for _ in range(n+1)] for _ in range(k+1)]

for i in range(1, k+1):
    for s in range(max(arr)):
        if d == 0:  # last move was to the right
            dp[i][s][0] = max(dp[i-1][s][0], dp[i-1][s-arr[0]][1])
        else:  # last move was to the left
            dp[i][s][1] = max(dp[i-1][s][1], dp[i-1][s+arr[0]][0])

print(max(dp[k][s][d]))

def max_score(n, k, z, arr):
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n):
        if i == 1:
            dp[i][0] = arr[0]
        elif i <= z:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + arr[i-1])
        else:
            for j in range(k+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j]
                elif j <= z and i > z:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + arr[i-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + arr[i-1])

    return dp[-1][-1]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z, arr))

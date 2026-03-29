def maximum_score(arr):
    n, k, z = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, min(2, n)):
        for j in range(min(k, i) + 1):
            if j <= z:
                dp[i][j] = max(dp[i-1][j], dp[i][min(j+1, z)] + arr[i])
            else:
                dp[i][j] = dp[i-1][j]

    for i in range(2, n):
        for j in range(min(k, i) + 1):
            if j <= z:
                dp[i][j] = max(dp[i-1][j], dp[i][min(j+1, z)] + arr[i])

    return dp[n-1][k]

t = int(input())
for _ in range(t):
    print(maximum_score(list(map(int, input().split()))))

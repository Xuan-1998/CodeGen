def maxScore(arr, k, z):
    n = len(arr)
    dp = [[0] * (n+1) for _ in range(k+1)]

    for i in range(1, k+1):
        for j in range(1, n+1):
            if i == 1:
                dp[i][j] = arr[j-1]
            elif i % z != 0 or j == 1:
                dp[i][j] = max(dp[i-1][j-1] + arr[j-1], dp[i-1][j+1] + arr[j])
            else:
                dp[i][j] = max(dp[i-1][j-1] + arr[j-1], dp[i-1][j-2] + arr[j-2])

    return dp[k][n]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(maxScore(arr, k, z))

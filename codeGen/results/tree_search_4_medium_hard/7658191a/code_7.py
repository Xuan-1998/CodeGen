def max_score(arr, n, k, z):
    dp = [[0]* (k+1) for _ in range(n)]
    for i in range(1, n):
        for j in range(min(i,z)+1):
            if j == 0:
                dp[i][j] = arr[i]
            else:
                dp[i][j] = max(dp[i-1][j-1] + arr[i], dp[i-1][j-1] - arr[i-1])
    return dp[n-1][k]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(arr, n, k, z))

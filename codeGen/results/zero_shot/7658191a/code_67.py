def solve(arr, k, z):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]
    for i in range(1, n):
        for j in range(min(i, k)):
            if j <= z:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + arr[i])
            else:
                dp[i][j] = dp[i-1][j-1] + arr[i]
    return max(dp[-1])

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(arr, k, z))

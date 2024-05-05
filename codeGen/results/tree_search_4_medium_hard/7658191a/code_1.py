def max_score(arr):
    n, k, z = map(int, input().split())
    dp = [[float('-inf')] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][0] = arr[i - 1]
    
    for j in range(1, k + 1):
        for i in range(1, n + 1):
            if j == 1:
                left = arr[i - 2] if i >= 2 and j <= z else float('-inf')
                right = arr[i] if i < n else float('-inf')
                dp[i][j] = max(dp[i - 1][j - 1] + left, dp[i - 1][j - 1] + right)
            else:
                if i >= 2 and j <= z:
                    left = arr[i - 2]
                else:
                    left = float('-inf')
                right = arr[i]
                dp[i][j] = max(dp[i - 1][j - 1] + left, dp[i - 1][j - 1] + right)
    
    return dp[n][k]

for _ in range(int(input())):
    print(max_score(list(map(int, input().split()))))

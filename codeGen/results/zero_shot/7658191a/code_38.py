def max_score(arr, k, z):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][0] = sum(arr[:i])
        
    for j in range(1, min(z + 1, k + 1)):
        dp[0][j] = arr[0]
        
    for i in range(1, n + 1):
        for j in range(1, min(k - (n - i), z + 1) + 1):
            if i >= 2:
                right_move = dp[i-1][j-1] + arr[i]
                left_move = dp[i-1][j-1] + arr[i-2]
                dp[i][j] = max(right_move, left_move)
            else:
                dp[i][j] = arr[0] if j == 1 else 0
    
    return dp[n][k]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(arr, k, z))

def max_score(a, k, z):
    n = len(a)
    dp = [[0] * (z + 1) for _ in range(k + 1)]
    
    # Base case: 0 moves
    for j in range(z + 1):
        dp[0][j] = a[0]
    
    # Fill up the dp array
    for i in range(1, k + 1):
        for j in range(min(i, z) + 1):
            if i > 1:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[j+1])
            else:
                dp[i][j] = a[0]
    
    # Return the maximum score
    return dp[k][z]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_score(a, k, z))

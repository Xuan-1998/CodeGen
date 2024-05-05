def max_score(n, k, z, a):
    dp = [[[0] * 3 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if j == 0:
                dp[i][j][0] = a[i]
            else:
                dp[i][j][0] = max(dp[i-1][j-1][0], a[i])
            if i > z+1 and j < min(k, i-z-2)+1:
                dp[i][j][1] = max(dp[i-1][j-1][1], a[i-1])
            else:
                dp[i][j][1] = -float('inf')
            if i < n-z and j < min(k, z+1)+1:
                dp[i][j][2] = max(dp[i+1][j-1][2], a[i+1])
            else:
                dp[i][j][2] = -float('inf')

    return max(max(dp[n-1][i]) for i in range(3))

# Read input from stdin
n, k, z = map(int, input().split())
a = list(map(int, input().split()))

print(max_score(n, k, z, a))

n, k, z = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[[0] * (z+1) for _ in range(k+1)] for _ in range(n)]

for i in range(2, n):
    for j in range(k+1):
        for z in range(min(j, z)+1):
            dp[i][j][z] = max(dp[i-1][j-1][z-1] + arr[i], 
                               dp[i-1][j][z] - arr[i])

max_score = 0
for j in range(k+1):
    max_score = max(max_score, dp[n-1][j])
print(max_score)

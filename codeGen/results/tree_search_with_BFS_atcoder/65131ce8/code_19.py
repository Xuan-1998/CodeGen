N = int(input())
d = list(map(int, input().split()))
MOD = 998244353

# Initialize dp array
dp = [[[0, 0] for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][1] = 1

# Count the number of vertices with each out-degree
cnt = [0 for _ in range(N+1)]
for i in range(N):
    cnt[d[i]] += 1

# Calculate dp array
for i in range(N):
    for j in range(i+1):
        for k in range(2):
            # Add the current vertex to a new subtree
            dp[i+1][j+1][1] = (dp[i+1][j+1][1] + dp[i][j][k]) % MOD
            # Add the current vertex to an existing subtree
            if k == 1 and j < cnt[i]:
                dp[i+1][j+1][1] = (dp[i+1][j+1][1] + dp[i][j][1] * (cnt[i] - j)) % MOD
            # Do not add the current vertex to a subtree
            if j < cnt[i+1]:
                dp[i+1][j][0] = (dp[i+1][j][0] + dp[i][j][k] * (cnt[i+1] - j)) % MOD

# Calculate the sum of the number of good vertices for all good trees
ans = 0
for i in range(N+1):
    for j in range(i+1):
        ans = (ans + dp[N][i][1]) % MOD

# Print the answer
print(ans)


n = int(input())
sequence = list(map(int, input().split()))
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(min(i, n), 0, -1):
        if sequence[i-1] == sequence[i-k]:
            dp[i][k] = max(dp[j-1][k-1] + (j-i) for j in range(i-k+1, i))
        else:
            dp[i][k] = max(dp[j-1][k-1] for j in range(i-k+1, i))

print(max(dp[i][i] for i in range(n)))

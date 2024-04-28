n = int(input())
arr = list(map(int, input().split()))
dp = [[[] for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i, n+1):
        if arr[i-1] <= j:
            dp[i][j] = (set([k for k in dp[i-1][j-k] if k>=0]) | set([k for k in dp[i-1][j]])) - set(dp[i-1])
        else:
            dp[i][j] = set(dp[i-1][j])

print(' '.join(map(str, sorted(set().union(*dp[-1])))))

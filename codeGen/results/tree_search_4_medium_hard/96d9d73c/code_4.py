from collections import defaultdict

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

dp = defaultdict(lambda: {j: False for j in range(K+1)})
for i in range(1, N+1):
    for j in range(min(i//K, K)+1):
        if all(A[k-1]-M <= A[m] <= A[k-1]+M for m in max(0, k-j), k)):
            dp[i][j] = any(dp[k-j][j-1] for k in range(j+1, i+1))
        else:
            dp[i][j] = False

print(any(dp[N][K]))

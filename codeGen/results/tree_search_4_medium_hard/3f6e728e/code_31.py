import sys; input = sys.stdin.readline
def find_upper_hemisphere(r):
    return N - (C - r)

dp = [[0] * (min(N, M) + 1) for _ in range(C+1)]
dp[0][0] = 1

for i in range(1, C+1):
    for j in range(min(N, M)+1):
        dp[i][j] = sum(dp[k][min(j-1, m)] for k in range(i) if find_upper_hemisphere(k) <= j)

print(*dp[-1], sep=' ')

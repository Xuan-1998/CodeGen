def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        upper = list(map(int, input().split()))
        lower = list(map(int, input().split()))

        dp = [[0] * (M+1) for _ in range(C+1)]
        dp[0][j] = 1 for j in range(M+1)

        for i in range(1, C+1):
            for j in range(min(N,M)+1):
                for k in range(1, min(i+1, C)+1):
                    if upper.count(k) <= N and lower.count(k) <= M:
                        dp[i][j] = (dp[i][j] + dp[max(0, i-k)][min(j, m+k)]) % (10**9+7)

        print(*dp[C], sep=' ')

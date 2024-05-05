import sys

def count_steady_tables(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[1] = [1] * (M + 1)
    
    for i in range(2, N + 1):
        for j in range(M + 1):
            for k in range(i):
                if k <= j:
                    dp[i][j] += dp[k][j - (M - 1) - k + 1]
                    
    return sum(dp[N])

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(count_steady_tables(N, M))

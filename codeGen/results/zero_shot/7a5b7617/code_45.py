import sys

def find_steady_tables():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(M + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i - 1][j] + j) % (10**9 + 7)
        print(sum([pow(2, i, 10**9 + 7) for i in range(N)]))

find_steady_tables()

import sys

def calculate_steady_tables():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(M + 1):
                if i == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i - 1][j] + j) % 1000000000
        print(sum(dp[N]))
        
calculate_steady_tables()

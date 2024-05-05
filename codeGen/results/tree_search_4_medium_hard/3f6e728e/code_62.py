from collections import defaultdict

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        dp = [[defaultdict(int) for _ in range(C+1)] for _ in range(C+1)]
        dp[0][0] = 1

        for i in range(1, N+1):
            for j in range(1, M+1):
                if U_i == 1 or L_j == 1:
                    dp[i][j] = (dp[i-1][0] + dp[0][j-1]) * 1
                else:
                    dp[i][j] = (dp[i-1][0] + dp[0][j-1]) * (dp[i-1][j-1] if i and j are greater than 0 else 1)

        for c in range(C+1):
            print((dp[N][c] + dp[c][M]) % (10**9+7), end=" ")
        print()

if __name__ == "__main__":
    solve()

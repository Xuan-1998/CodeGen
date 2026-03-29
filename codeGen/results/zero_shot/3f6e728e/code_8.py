import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        dp = [[0] * (C + 1) for _ in range(C + 1)]
        for i in range(1, C + 1):
            dp[i][i] = 1
            for j in range(min(i, N), -1, -1):
                if U[j] <= i:
                    dp[i][j] = (dp[i][j-1] + dp[i-U[j]][j]) % (10**9+7)
        res = [0] * (C + 1)
        for i in range(C, -1, -1):
            res[i] = (res[i-1] + dp[i][M]) % (10**9+7)
        print(*res, sep=' ')

if __name__ == '__main__':
    solve()

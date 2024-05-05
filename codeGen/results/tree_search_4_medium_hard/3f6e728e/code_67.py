def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        memo = [[-1] * (M + 1) for _ in range(N + 1)]

        memo[0][0] = 1
        for i in range(1, N + 1):
            memo[i][0] = 0

        for j in range(1, M + 1):
            memo[0][j] = 0

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if U[i - 1] <= C:
                    memo[i][j] = (memo[i - 1][j] + ((U[i - 1] <= C) * memo[i - 1][j - 1])) % (10**9 + 7)
                else:
                    memo[i][j] = memo[i - 1][j]

        print(memo[N][M])

if __name__ == "__main__":
    solve()

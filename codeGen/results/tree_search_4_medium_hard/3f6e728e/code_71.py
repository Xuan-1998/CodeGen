def solve():
    T = int(input())
    MOD = 10**9 + 7

    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        dp = [[0] * (C + 1) for _ in range(N + M + 1)]

        def dfs(i, j):
            if i == N or i == M:
                return 1
            if U[i-1] < L[0]:
                return 0
            ans = sum(dfs(k, j-1) * (U[k] == U[i]) for k in range(i+1, N+1))
            return (ans + M - j) % MOD

        print((dfs(N, C)) % MOD)

if __name__ == '__main__':
    solve()

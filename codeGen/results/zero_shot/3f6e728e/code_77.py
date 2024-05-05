import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        dp = [0] * (C + 1)
        dp[0] = 1

        for i in range(N):
            for j in range(C, U[i] - 1, -1):
                dp[j] += dp[j - 1]
        for i in range(M):
            for j in range(L[i], C):
                dp[j] += dp[j - 1]

        result = [0] * (C + 1)
        result[0] = 1
        for i in range(1, C + 1):
            if i <= U[-1]:
                result[i] += result[i - 1]
            if i <= L[-1]:
                result[i] += result[i - 1]

        print(*result, sep=' ')

if __name__ == "__main__":
    solve()

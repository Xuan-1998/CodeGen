import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        dp = [0] * (C + 1)
        dp[0] = 1

        for i in range(1, C + 1):
            dp[i] = 1
            for j in range(N):
                if U[j] <= i:
                    dp[i] *= (i - U[j]) // L[j]
            for j in range(M):
                if L[j] < i:
                    dp[i] *= (i - L[j])
            dp[i] %= 10**9 + 7

        print(*dp, sep=' ')

if __name__ == '__main__':
    solve()

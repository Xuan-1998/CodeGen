import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, C = map(int, sys.stdin.readline().split())
        U = list(map(int, sys.stdin.readline().split()))
        L = list(map(int, sys.stdin.readline().split()))
        U.sort()
        L.sort()
        MOD = 10**9 + 7
        dp = [0] * (C + 1)
        for i in range(C):
            if i < N:
                dp[i + 1] += dp[i]
            if i < M:
                dp[i + 1] += dp[i]
            dp[i + 1] %= MOD
        print(' '.join(map(str, dp)))

if __name__ == '__main__':
    solve()

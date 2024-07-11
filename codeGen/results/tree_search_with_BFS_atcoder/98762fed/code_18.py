import sys
from math import factorial

MOD = 998244353

def C(n, r):
    if r > n or r < 0:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def solve(N, M):
    dp = [[0]*(M+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N+1):
        for j in range(M+1):
            for p in range(i+1):
                for q in range(j+1):
                    dp[i][j] += dp[p][q] * dp[i-p][j-q] * 4 * C(i, p) * C(j, q)
                    dp[i][j] %= MOD
    return dp[N][M]

def main():
    N, M = map(int, sys.stdin.readline().split())
    print(solve(N, M))

if __name__ == "__main__":
    main()


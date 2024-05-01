import sys
mod = 10**9 + 7

def solve(m, N):
    dp = [[0] * (m+1) for _ in range(N+1)]
    
    for N in range(1, N+1):
        if N == 0:
            dp[N][0] = 1
        else:
            for i in range(m):
                if N >= array[i]:
                    dp[N][i+1] += dp[N-array[i]][i]
                    dp[N][i+1] %= mod
    
    print(dp[N][m], mod=mod)

# Read input from standard input.
m, N = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

solve(m, N)

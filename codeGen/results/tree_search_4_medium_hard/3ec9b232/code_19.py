import sys

def solve():
    n = int(input())
    m = list(map(int, input().split()))
    
    MOD = 10**9 + 7
    
    dp = [[0] * (1 << n) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for p in range(1 << n):
            if m[i-1] <= i:
                for s in range(p):
                    if (s & p) == 0 or m[i-1] > m[s]:
                        dp[i][p] = (dp[i][p] + dp[i-1][s]) % MOD
    print(dp[n][-1])

if __name__ == "__main__":
    solve()

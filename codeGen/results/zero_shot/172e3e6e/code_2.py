import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    MOD = 10**9 + 7
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(min(i, n - i), -1, -1):
            if a[i-1] % (i+1) == 0:
                dp[i][j] = dp[i-1][max(j-1, 0)] if j > 0 else 1
                dp[i][j] %= MOD
    
    total_good = sum(dp[i][n-i] for i in range(1, n + 1))
    print(total_good % MOD)

if __name__ == "__main__":
    solve()

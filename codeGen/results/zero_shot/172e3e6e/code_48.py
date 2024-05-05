import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    MOD = 10**9 + 7
    
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        if a[i - 1] % i == 0:
            dp[i] += dp[i - 1]
        dp[i] %= MOD
    
    print(sum(dp) % MOD)

if __name__ == "__main__":
    solve()

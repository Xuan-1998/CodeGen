import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    MOD = 10**9 + 7
    
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        if a[i] % (i + 1) == 0:
            dp[i + 1] += dp[i]
        dp[i + 1] %= MOD
    
    print(dp[-1])

if __name__ == "__main__":
    solve()

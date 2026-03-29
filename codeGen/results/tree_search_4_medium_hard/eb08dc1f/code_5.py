import sys

def solve(n):
    MOD = int(1e9) + 7
    dp = [0] * (n + 1)
    
    for i in range(10):
        for j in range(min(i+1, n), 0, -1):
            for k in range(j-1, 0, -1):
                dp[j] += dp[k]
            if j == 1:
                dp[1] = (dp[1] + 1) % MOD
            else:
                dp[j] %= MOD
    
    return [str(int(dp[i]) % MOD) for i in range(1, n+1)]


if __name__ == "__main__":
    n = int(input())
    print(*solve(n), sep=' ')

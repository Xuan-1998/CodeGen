import sys

def beauty_contest(t, l, r):
    MOD = 10**9 + 7
    
    # Precompute f(m) for m <= r
    dp = [[0] * (r + 1) for _ in range(t + 1)]
    
    for i in range(2, t + 1):
        for j in range(l, r + 1):
            if i == 2:
                # Base case: f(n) = 0 for n = 1
                dp[i][j] = (dp[i - 1][j - 1] * (i - 1) % MOD + (j - l + 1) % MOD) % MOD
            else:
                # Combine results of smaller instances
                dp[i][j] = (dp[i - 1][j - 1] * i % MOD + dp[i - 2][j - 2] * (i - 2) % MOD) % MOD
    
    # Calculate the final result
    ans = 0
    for j in range(l, r + 1):
        ans += (dp[t][j] * (r - l + 1) % MOD - j) % MOD
    
    return ans % MOD

if __name__ == "__main__":
    t, l, r = map(int, input().split())
    print(beauty_contest(t, l, r))

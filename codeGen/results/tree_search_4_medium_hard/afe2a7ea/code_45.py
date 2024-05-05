import sys

def solve():
    n = int(input())
    
    MOD = 998244353
    
    dp = [[[0]*n for _ in range(1<<n)] for _ in range(n+1)]
    
    # Initialize base case: no towers can send signal to town 0.
    for j in range(2**n):
        dp[0][j][0] = 1
    
    for i in range(1, n+1):
        for mask in range(1<<i):
            # Calculate the number of valid configurations that can be extended
            # to town i from previous states.
            for k in range(i-1, -1, -1):
                if not ((mask>>k)&1):
                    for prev_mask in range(1<<k):
                        dp[i][mask|(1<<k)][k] += dp[k][prev_mask][i-k]
                        dp[i][mask|(1<<k)][k] %= MOD
    
    # Calculate the probability of finding a way to set signal powers.
    ans = 0
    for i in range(n+1):
        for j in range(1<<n):
            if not ((j>>i)&1) and dp[n][j][i]:
                ans += 1
                ans %= MOD
    
    print(ans)

if __name__ == "__main__":
    solve()

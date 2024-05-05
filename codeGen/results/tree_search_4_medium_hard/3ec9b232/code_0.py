import sys

def solve():
    n = int(input())
    m = list(map(int, input().split()))
    
    # Initialize DP table
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[0][0] = 1
    
    for i in range(1, n+1):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][0]
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % (10**9 + 7)
    
    # Calculate the answer
    ans = 0
    for i in range(n+1):
        if m.count(i) > 0:
            ans += dp[n][m.count(i)]
            ans %= (10**9 + 7)
    
    print(ans)

if __name__ == "__main__":
    solve()

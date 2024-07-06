MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 1
    
    # Fill DP table
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i):
                if d[k - 1] > 0 and d[k - 1] <= i - 1:
                    dp[i][j] = (dp[i][j] + dp[k][j - 1] * dp[i - k][1]) % MOD
    
    # Compute the final answer
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    
    print(result)

if __name__ == "__main__":
    solve()


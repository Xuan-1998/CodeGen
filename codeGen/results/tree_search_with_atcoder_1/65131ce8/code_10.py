python
MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    if d[0] < 1 or sum(d) != N - 1:
        print(0)
        return
    
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: one way to have 0 good vertices
    
    # For each vertex, compute the DP values
    for i in range(1, N + 1):
        for k in range(N + 1):
            dp[i][k] = dp[i-1][k]
            if k > 0 and d[i-1] > 0:
                dp[i][k] = (dp[i][k] + dp[i-1][k-1]) % MOD
    
    # Sum the number of good vertices for all good trees
    result = sum(dp[N]) % MOD
    
    print(result)

if __name__ == "__main__":
    main()


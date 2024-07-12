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
    
    # Fill the DP table
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] * (i - 1)) % MOD
    
    # Calculate the number of good vertices for all good trees
    result = 0
    for i in range(1, N + 1):
        result = (result + dp[N][i] * i) % MOD
    
    print(result)



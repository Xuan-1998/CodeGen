MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize dp array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 1
    
    # Fill dp array
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i):
                if d[k - 1] > 0:
                    dp[i][j] = (dp[i][j] + dp[i - k][j - 1] * d[k - 1]) % MOD
    
    # Sum the number of good vertices for all good trees
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    
    print(result)



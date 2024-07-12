MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # dp[i][j] will store the number of ways to form a subtree with i vertices and j good vertices
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 1
    
    # Fill dp table
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i):
                if d[k - 1] > 0:
                    dp[i][j] = (dp[i][j] + dp[k][j - 1] * dp[i - k][1]) % MOD
    
    # Calculate the result
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    
    print(result)



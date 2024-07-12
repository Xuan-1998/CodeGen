python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # dp[i][j] - number of ways to form a subtree with i vertices and j good vertices
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            for k in range(i):
                for m in range(j):
                    dp[i][j] = (dp[i][j] + dp[k][m] * dp[i - 1 - k][j - 1 - m]) % MOD
    
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    print(result)



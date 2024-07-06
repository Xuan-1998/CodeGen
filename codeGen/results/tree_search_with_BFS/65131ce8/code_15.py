python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # dp[i][j] will be the number of ways to form a subtree rooted at i with exactly j good vertices
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][1] = 1
    
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            if d[i - 1] == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i - 1][j - 1] * d[i - 1]) % MOD
    
    result = sum(dp[N]) % MOD
    print(result)



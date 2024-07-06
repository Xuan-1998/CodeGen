python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][1] = 1  # Base case: one node, one good vertex
    
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i):
                if d[k - 1] > 0:
                    dp[i][j] = (dp[i][j] + dp[i - k][j - 1] * dp[k][1]) % MOD
    
    result = sum(dp[N]) % MOD
    print(result)



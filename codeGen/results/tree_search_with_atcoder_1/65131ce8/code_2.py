python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    dp = [[0] * (N) for _ in range(N + 1)]
    dp[1][0] = 1
    
    for i in range(2, N + 1):
        for j in range(N):
            for k in range(1, i):
                if j >= d[k - 1]:
                    dp[i][j] = (dp[i][j] + dp[k][d[k - 1]] * dp[i - k][j - d[k - 1] - 1]) % MOD
    
    result = 0
    for i in range(1, N + 1):
        result = (result + dp[N][d[i - 1]]) % MOD
    
    print(result)



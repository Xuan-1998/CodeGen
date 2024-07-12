MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    good_count = [[0] * (N + 1) for _ in range(N + 1)]
    
    dp[1][0] = 1
    good_count[1][0] = 1
    
    for i in range(2, N + 1):
        for j in range(N):
            if j > i - 1:
                continue
            for k in range(1, i):
                dp[i][j] = (dp[i][j] + dp[k][j-1] * dp[i-k][0]) % MOD
                good_count[i][j] = (good_count[i][j] + good_count[k][j-1] + good_count[i-k][0]) % MOD
    
    result = 0
    for i in range(1, N + 1):
        for j in range(N):
            if d[i-1] == j:
                result = (result + good_count[i][j]) % MOD
    
    print(result)



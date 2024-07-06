MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    if sum(d) != N-1 or d[0] < 1:
        print(0)
        return
    
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][1] = 1
    
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i):
                for l in range(1, j + 1):
                    dp[i][j] = (dp[i][j] + dp[k][l] * dp[i - k][j - l]) % MOD
    
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    print(result)

if __name__ == "__main__":
    solve()


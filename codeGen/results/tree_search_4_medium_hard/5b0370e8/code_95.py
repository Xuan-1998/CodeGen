def solve():
    t = int(input())
    MOD = 10**9 + 7
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n, -1, -1):
            for j in range(k, -1, -1):
                for m in range(i):
                    if ((m >> k) & 1) == ((i >> k) & 1):
                        dp[i][j] = (dp[m][j-1] + dp[i][j]) % MOD
        result = sum([sum([dp[i][k-1] * ((1 << i) - 1).bit_length() % MOD for i in range(k)]) % MOD for _ in range(n)])
        print(result % MOD)

if __name__ == "__main__":
    solve()

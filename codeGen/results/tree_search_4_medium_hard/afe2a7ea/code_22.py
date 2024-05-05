def find_probability():
    n = int(input())
    MOD = 998244353

    dp = [[False] * (n+1) for _ in range(n+2)]

    for i in range(1, n+1):
        for j in range(min(i-1, n)):
            for k in range(j+1, i):
                if not dp[k][j]:
                    dp[i][j] = True
                    break

    ans = 0
    for j in range(n+1):
        if dp[n][j]:
            ans += 1
            break

    return (ans * pow(2, n, MOD)) % MOD


if __name__ == "__main__":
    print(find_probability())

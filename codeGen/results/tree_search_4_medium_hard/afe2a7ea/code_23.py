def solve(n):
    MOD = 998244353
    dp = [False] * (n + 2)
    for i in range(n + 2):
        if i == 0 or i == n + 1:
            dp[i] = True
        else:
            for j in range(i):
                if not dp[j]:
                    dp[i] = dp[i] or any((j, k) for k in range(j + 1, i + 1))
                    break

    return (dp[n] and 1) % MOD

if __name__ == "__main__":
    n = int(input())
    print(solve(n))

def solve():
    a, b = map(int, input().split())
    MOD = 10**9 + 7

    dp = [0] * (len(bin(a)) + len(bin(b)))
    for i in range(len(bin(a)) + len(bin(b))):
        if i == 0:
            dp[i] = a ^ b
        else:
            dp[i] = (dp[i-1] + ((a >> (i-1)) ^ b) % MOD) % MOD

    print(sum(dp) % MOD)

if __name__ == "__main__":
    solve()

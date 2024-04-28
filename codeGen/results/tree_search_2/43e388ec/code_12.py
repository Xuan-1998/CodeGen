def solve():
    k = 314159
    MOD = 10**9 + 7

    dp = [0] * (k + 1)
    b = int(input())  # read binary number b from input
    for i in range(k + 1):
        if b & 1:  # check least significant bit of b
            dp[i] = dp[i - 1] + ((a ^ (b >> 1)) % MOD) if i else a % MOD
        else:
            dp[i] = dp[i - 1]
        b >>= 1

    return sum(dp) % MOD

if __name__ == "__main__":
    print(solve())

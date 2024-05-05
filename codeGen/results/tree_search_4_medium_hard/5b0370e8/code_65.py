import sys

def solve():
    n = int(input())
    dp = [[[0] * 1000003 for _ in range(2**20)] for _ in range(n + 1)]
    MOD = 10**9 + 7

    for i in range(n):
        x = int(input())
        for j in range(i, -1, -1):
            y = dp[j][x ^ (i - j)][(x & ((1 << k) - 1)) % (2**20)]
            dp[i][x ^ (i + 1)][x & ((1 << k) - 1)] += y
        k = i.bit_length()
    print(sum(dp[-1]) % MOD)

if __name__ == "__main__":
    solve()

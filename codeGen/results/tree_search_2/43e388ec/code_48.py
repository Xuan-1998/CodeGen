import sys

def solve():
    k = int(input())
    a = int(input(), 2)
    b = int(input(), 2)

    MOD = 10**9 + 7
    dp = [0] * (k + 1)

    for i in range(k + 1):
        if i == 0:
            dp[i] = a ^ b
        else:
            new_dp = dp[i - 1]
            for j in range(i):
                new_dp ^= ((a >> j) & 1) * (b >> k - 1 - j)
            dp[i] = new_dp % MOD

    print(sum(dp))

if __name__ == "__main__":
    solve()

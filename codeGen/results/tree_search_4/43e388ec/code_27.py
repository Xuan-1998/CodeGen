import sys

def solve(a, b):
    MOD = 10**9 + 7
    dp = [0] * (min(a, b) + 1)

    for i in range(1, min(a, b) + 1):
        dp[i] = (b & 1) * ((2 ** i) - 1) + dp[i-1]

    return sum(dp[:a]) % MOD

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(solve(a, b))

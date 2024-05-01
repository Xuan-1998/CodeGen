mod = 10**9 + 7

def solve():
    a, b = map(int, input().split())
    k = int(2 ** 30)  # assuming the maximum value of i is 2^30

    dp = [0] * (k + 1)
    dp[0] = a ^ b
    for i in range(1, k + 1):
        dp[i] = (dp[i-1] << 1) ^ (b >> (i-1))

    return sum(dp) % mod

print(solve())

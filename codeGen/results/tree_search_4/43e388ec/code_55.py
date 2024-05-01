import sys

# Precompute powers of 2 up to 2^31
powers_of_2 = [pow(2, i) for i in range(32)]

def solve():
    a, b = map(int, input().split())
    dp = [0] * (314159 + 1)
    dp[0] = a ^ b

    for i in range(1, 314160):
        if i % 31 == 0:
            dp[i] = (a ^ ((b >> (i // 31)) & (powers_of_2[i // 31 - 1]))) % (10**9 + 7)
        else:
            dp[i] = ((dp[i-1] << 1) ^ b) % (10**9 + 7)

    return sum(dp[:314160]) % (10**9 + 7)

print(solve())

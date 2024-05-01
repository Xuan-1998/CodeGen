import sys

def solve():
    a, b = map(int, input().split())
    dp = [0] * (314160 + 1)
    dp[0] = a
    for i in range(1, 314160):
        dp[i] = (a ^ ((b >> (i & 31)) | (dp[(i - 1) % 32] << (31 - (i & 31)))))
    return str(dp[-1] % (10**9 + 7))

print(solve())

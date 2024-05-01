import sys

a = int(input(), 2)
b = int(input(), 2)

dp = [-1] * (315160 + 1)
dp[0] = 0

for i in range(1, 315161):
    if (i & (i - 1)) == 0:  # i is a power of 2
        if ((a >> i.bit_length() - i) ^ (b >> i.bit_length() - i)).bit_length():
            dp[i] = dp[i // 2]
    else:
        dp[i] = dp[i - 1]

print((dp[314159] + 7) % (10**9 + 7))

import sys

a, b = [int(x) for x in input().split()]
DP = [0] * (314160)
DP[0] = a ^ b

for i in range(1, 314160):
    DP[i] = (DP[i-1] ^ ((b % 2) & 1)) + ((b >> 1) & 1)

print(sum(DP) % (10**9 + 7))

import sys

input()
a = int(input())
b = int(input())

DP = [0] * (314160)
DP[0] = a

for i in range(1, 314161):
    if i == 0:
        DP[i] = a
    else:
        DP[i] = (a & (1 << i)) and (DP[i-1] ^ (b >> i)) or DP[i-1]

ans = sum(DP[:]) % (10**9 + 7)
print(ans)

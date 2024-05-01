import sys

mod = 10**9 + 7

a, b = map(int, input().split())
DP = [a]
for i in range(b.bit_length()):
    if (b >> i & 1):
        DP.append((DP[-1] ^ (DP[-1] << (i+1))) + b)
    else:
        DP.append(DP[-1])
ans = sum(DP) % mod
print(ans)

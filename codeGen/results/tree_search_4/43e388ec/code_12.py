import sys

a, b = [int(x) for x in input().split()]
dp = [0] * (314160)
ans = 0

for i in range(314160):
    ans += a ^ ((b >> (i % 9)) & 1)
    ans %= 10**9 + 7
print(ans)

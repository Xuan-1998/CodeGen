from collections import deque

a, b = map(int, input().split())
dp = [[0] * (b.bit_length() + 1) for _ in range(a.bit_length() + 1)]

ans = 0
for i in range(a.bit_length()):
    ans = ((ans << 1) | (a & 1)) % (10**9 + 7)
    for j in range(b.bit_length()):
        dp[i][j] = ans

res = 0
for i in range(a.bit_length() + 1):
    temp = sum(dp[i])
    res = ((res + temp) % (10**9 + 7))
print(res)

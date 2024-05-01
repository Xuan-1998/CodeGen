import sys

mod = 10**9 + 7
b_len, _ = map(int, input().split())
a, b = int(input()), [int(x) for x in bin(b)[2:].zfill(b_len)]
dp = [[0] * (b_len+1) for _ in range(a.bit_length()+1)]

for j in range(b_len+1):
    dp[0][j] = b[j]

for i in range(1, a.bit_length()+1):
    for j in range(b_len+1):
        if i > 0:
            dp[i][j] = (dp[i-1][(j+1)%b_len] + a[i-1]) ^ b[(i+j)%b_len]
        else:
            dp[i][j] = a[j]

ans = sum(dp[-1])
print(ans % mod)

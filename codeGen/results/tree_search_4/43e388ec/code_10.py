code_block = '''
import sys

m = 10**9 + 7
dp = [[0] * (m) for _ in range(32)]

for p in range(31, -1, -1):
    dp[p][0] = int('1' * p, 2)
    
for i in range(m):
    dp[31][i] = i

for j in range(2, m):
    dp[0][j] = j - (j >> 1)

for p in range(1, 32):
    for i in range(j := 2**(p-1), m):
        if p == 1:
            dp[p][i] = min(dp[p-1][i-1], dp[p-1][i]) | int('1' * p, 2)
        else:
            dp[p][i] = min(dp[p-1][i-1], dp[p-1][i]) | (dp[31][i] >> (p-1))
            
for _ in range(314159):
    a, b = map(int, input().split())
    print((dp[30][b] ^ (a << b)) % m)
'''

print(code_block)

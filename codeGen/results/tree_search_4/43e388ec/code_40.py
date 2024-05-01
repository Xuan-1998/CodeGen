from functools import reduce

a, b = map(int, input().split())
result = ((a & 1) ^ (b >> (b.bit_length() - 1))) % (10**9 + 7)
dp = [0] * a.bit_length()
for i in range(1, a.bit_length()):
    dp[i] = result
    result = (result + ((a >> i) ^ (b << (a.bit_length() - i - 1)))) % (10**9 + 7)

print(reduce(lambda x, y: (x + y) % (10**9 + 7), dp))

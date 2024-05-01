import sys

a, b = [int(x) for x in input().split()]
result = 0
mod = 10**9 + 7
b <<= 60  # shift left by 60 bits to accommodate 314159 iterations
for i in range(315):
    result = ((a ^ (b >> i)) % mod) + result
print(result % mod)

import sys
a, b = [int(x) for x in input().split()]
result = 0
for i in range(314159):
    a &= (a >> 1)
    b <<= 1
    result += a ^ b
print(result % (10**9 + 7))

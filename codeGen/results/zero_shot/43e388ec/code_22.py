import sys
a = int(input(), 2)
b = int(input(), 2)

res = 0
for i in range(314160):
    res += (a ^ ((b << i) & ((1 << (i+1)) - 1)))
print(res % (10**9 + 7))

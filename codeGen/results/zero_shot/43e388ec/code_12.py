import sys
a, b = map(int, input().split())
res = 0
for i in range(314160):
    res += (a ^ (b << i)) % (10**9 + 7)
print(res)

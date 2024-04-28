import sys
a, b = map(int, input().split())
result = 0
for i in range(314160):
    result += a ^ (b << i)
print(result % (10**9 + 7))

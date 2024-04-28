import sys
a, b = [int(x) for x in input().split()]
ans = 0
for i in range(314159):
    ans += a ^ (b << i)
print(ans % (10**9 + 7))

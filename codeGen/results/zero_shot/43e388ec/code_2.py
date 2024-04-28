import sys
a, b = [int(x, 2) for x in input().split()]
ans = sum((a ^ (b << i)) % (10**9 + 7) for i in range(314159))
print(ans)

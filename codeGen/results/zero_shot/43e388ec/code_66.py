a, b = map(int, input().split())
res = 0
for i in range(314159):
    res += (a ^ (b << i)) % (10**9 + 7)
print(res)

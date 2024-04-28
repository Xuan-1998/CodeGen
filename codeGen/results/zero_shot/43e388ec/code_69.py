a, b = map(int, input().split())
total = 0
for i in range(314160):
    total += (a ^ (b << i)) % (10**9 + 7)
print(total)

a, b = [int(i) for i in input().split()]
result = 0
for i in range(314160):
    result += (a ^ ((b << i) & ((1 << 30) - 1))) % (10**9 + 7)
print(result % (10**9 + 7))

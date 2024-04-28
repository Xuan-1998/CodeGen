a = int(input(), 2)
b = int(input(), 2)

total = 0
for i in range(314160):
    total += a ^ (b << i)

print(total % (10**9 + 7))

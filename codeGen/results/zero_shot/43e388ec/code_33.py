a = int(input(), 2)
b = int(input(), 2)

total = 0
for i in range(314159):
    total += (a ^ ((b << i) & 1))
print(total % (10**9 + 7))

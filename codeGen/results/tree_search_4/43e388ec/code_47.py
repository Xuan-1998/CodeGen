a = int(input(), 2)
b = int(input(), 2)

result = 0
for i in range(31):
    result += (a ^ ((b >> i) & 1)) % (10**9 + 7)

print(result % (10**9 + 7))

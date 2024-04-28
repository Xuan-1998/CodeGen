a = int(input(), 2)
b = int(input(), 2)

result = 0
for i in range(314159):
    b <<= 1
    result += a ^ b

print(result % (10**9 + 7))

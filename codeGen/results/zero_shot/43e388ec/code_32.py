a = int(input(), 2)
b = int(input(), 2)

result = 0
for i in range(314159):
    x = a ^ (b << i)
    result = (result + x) % (10**9 + 7)

print(result)

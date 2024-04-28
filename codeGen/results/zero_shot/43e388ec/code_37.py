a = int(input(), 2)
b = int(input(), 2)

result = 0
for i in range(314160):
    result += (a ^ (b << i)) % (10**9 + 7)

print(result)

a = int(input(), 2)
b = int(input(), 2)

result = 0
for i in range(314160):
    temp = a ^ (b << i)
    result += temp

print(result % (10**9 + 7))

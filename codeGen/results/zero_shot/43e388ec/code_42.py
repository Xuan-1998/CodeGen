a = int(input())
b = int(input())

result = 0
for i in range(314160):
    result += (a ^ (b << i)) % (10**9 + 7)

print(result)

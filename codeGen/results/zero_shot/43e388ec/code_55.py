a = int(input())
b = int(input())

result = 0
for i in range(314160):
    if ((a >> i) & 1) ^ (b & 1):
        result += 2 ** i

print(result % (10**9 + 7))

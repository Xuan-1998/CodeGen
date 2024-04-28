a, b = map(int, input().split())
result = 0
for i in range(314159):
    result += (a ^ (b << i)) % (10**9 + 7)
print(result)

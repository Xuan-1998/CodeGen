a = int(input(), 2)
b = int(input(), 2)

result = 0
for i in range(314159):
    if (b >> i) & 1:
        result ^= a
    result %= 10**9 + 7

print(result)

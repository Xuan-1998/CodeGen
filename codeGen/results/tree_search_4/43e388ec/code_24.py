a, b = map(int, input().split())
dp_a = [0] * (b.bit_length() + 1)
dp_b = [0] * (a.bit_length() + 1)

for i in range(b.bit_length(), -1, -1):
    dp_a[i] = ((10**9 + 7) + dp_a[i]) % (10**9 + 7)

for i in range(a.bit_length()):
    if a & (1 << i):
        for j in range(max(a.bit_length() - i - 1, b.bit_length()), -1, -1):
            dp_b[j] = ((dp_b[j] + 1) % (10**9 + 7)) if (b >> j) & 1 else (dp_b[j])
    else:
        for j in range(max(a.bit_length() - i - 1, b.bit_length()), -1, -1):
            dp_b[j] = ((10**9 + 7) + dp_b[j]) % (10**9 + 7)

result = 0
for i in range(min(b.bit_length(), a.bit_length()) + 1):
    result = ((10**9 + 7) + (dp_a[i] ^ dp_b[i])) % (10**9 + 7)

print(result)

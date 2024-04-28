a = int(input(), 2)
b = int(input(), 2)

ans = 0
for _ in range(314159):
    b <<= 1
    if a & 1:
        b ^= a
    a >>= 1
    ans += b
print(ans % (10**9 + 7))

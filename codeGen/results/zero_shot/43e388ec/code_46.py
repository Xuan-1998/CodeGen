a = int(input())
b = int(input())

ans = 0
for _ in range(314159):
    b = (b << 1) | a
    ans += b
print(ans % (10**9 + 7))

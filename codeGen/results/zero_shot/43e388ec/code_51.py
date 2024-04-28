a = int(input(), 2)
b = int(input(), 2)

ans = 0
for i in range(314159):
    ans += (a ^ (b << i)) % (10**9 + 7)

print(ans)

a = int(input(), 2)
b = int(input(), 2)

ans = 0
for i in range(314160):
    xored = a ^ (b << i)
    ans += xored
    ans %= 10**9 + 7

print(ans)

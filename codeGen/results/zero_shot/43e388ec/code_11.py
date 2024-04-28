a = int(input(), 2)
b = int(input(), 2)

ans = 0
for i in range(314160):
    ans += (a ^ (b << i))
print(ans % (10**9 + 7))

a, b = map(int, input().split())
ans = 0
for i in range(314160):
    ans += (a ^ ((b << i) & 1))
print(ans % (10**9 + 7))

a = int(input())
b = int(input())

ans = 0
for i in range(314160):
    ans += (a ^ (b << i)) % (10**9 + 7)

print(ans)

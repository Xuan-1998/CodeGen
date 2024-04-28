a = int(input())
b = int(input())

ans = 0
for i in range(315159):
    x = (a & (1 << i)) | ((b >> i) & 1)
    ans += x
    ans %= 10**9 + 7

print(ans)

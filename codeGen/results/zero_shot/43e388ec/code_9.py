a, b = map(int, input().split())
ans = 0
for _ in range(314159):
    ans += (a ^ (b << 1))
print(ans % (10**9 + 7))

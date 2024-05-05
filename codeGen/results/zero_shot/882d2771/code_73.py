python
t = int(input())
l, r = map(int, input().split())

# calculate f(n) for l <= n <= r
f = [0] * (r + 1)
for i in range(2, r + 1):
    if i % 2 == 0:
        f[i] = f[i // 2]
    else:
        f[i] = f[(i - 1) // 2] + 1

# calculate the expression
ans = 0
for i in range(t):
    ans += f[l + i]

print(ans % (10**9 + 7))

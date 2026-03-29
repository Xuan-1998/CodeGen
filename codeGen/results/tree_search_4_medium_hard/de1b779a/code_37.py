n, m, c0, d0 = map(int, input().split())
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())

print(dp(0, n))

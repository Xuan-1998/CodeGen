n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))
stuffings.sort(key=lambda x: (x[3] - x[2]) / x[1], reverse=True)
buns = []
for ai, bi, ci, di in stuffings:
    if n >= bi and c0 >= ci:
        buns.append(min(n // bi, c0 // ci))
max_profit = d0 + sum(di * bun for bun in buns)
print(max_profit)

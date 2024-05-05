n = int(input())
m = int(input())
c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))
stuffings.sort(key=lambda x: (x[3] - x[1]) / x[2])
max_profit = d0
remaining_dough = c0
for ai, bi, ci, di in stuffings:
    while remaining_dough >= ci:
        max_profit += di
        remaining_dough -= ci
        if remaining_dough < 0:  # out of dough or stuffings
            break
print(max_profit)

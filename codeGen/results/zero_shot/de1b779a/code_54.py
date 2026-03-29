n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

max_profit = d0 * n

for ai, bi, ci, di in stuffings:
    max_buns_with_stuffing = min(n // ci, ai // bi)  # Ceiling division
    profit_with_stuffing = max_buns_with_stuffing * di
    max_profit = max(max_profit, profit_with_stuffing)

print(max_profit)

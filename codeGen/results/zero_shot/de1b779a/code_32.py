n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

stuffings.sort(key=lambda x: (x[3] - x[1]) / x[2], reverse=True)

max_profit = 0
while n > 0 and stuffings:
    ai, bi, ci, di = stuffings.pop(0)
    num_buns = min(n, ci)  
    profit = (num_buns * (di - bi)) + d0
    max_profit = max(max_profit, profit)
    n -= num_buns * ci

if n > 0:
    num_buns = min(n, c0)
    max_profit += (num_buns * d0)

print(max_profit)

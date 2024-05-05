n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

def max_profit(scenario):
    if scenario == 'no_stuffing':
        return n * d0 - c0
    else:
        profit = 0
        for ai, bi, ci, di in stuffings:
            buns_made = min(n // (bi + ci), ai // bi)
            profit += buns_made * di - (n // (bi + ci)) * c0
            n -= buns_made * (bi + ci)
        return profit

no_stuffing_profit = max_profit('no_stuffing')
with_stuffing_profit = 0
for ai, bi, ci, di in stuffings:
    buns_made = min(n // (bi + ci), ai // bi)
    with_stuffing_profit += buns_made * di - (n // (bi + ci)) * c0
    n -= buns_made * (bi + ci)

max_profit = max(no_stuffing_profit, with_stuffing_profit)
print(max_profit)

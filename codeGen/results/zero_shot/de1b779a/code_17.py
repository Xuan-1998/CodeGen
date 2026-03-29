import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    stuffings.append({'ai': ai, 'bi': bi, 'ci': ci, 'di': di})

max_profit = 0
for stuffing in stuffings:
    # Calculate the profit for this stuffing
    profit_for_this_stuffing = min(stuffing['ai'], n - c0) * (d0 + stuffing['ci'])
    if profit_for_this_stuffing > max_profit:
        max_profit = profit_for_this_stuffing

print(max_profit)

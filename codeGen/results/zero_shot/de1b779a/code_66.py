n, m, c0, d0 = map(int, input().split())
max_profit = 0

for _ in range(m):
    ai, bi, ci, di = map(int, input().split())

    # Check if there is enough dough for an unstuffed bun
    if n >= c0:
        max_profit += d0

    # Check if there are at least 'ai' grams of the current stuffing left
    if n - ai >= 0 and ai - bi >= 0:
        # If there is enough dough and required amount of stuffing for a bun with this stuffing, make a bun and sell it
        max_profit += di

    n -= c0

print(max_profit)

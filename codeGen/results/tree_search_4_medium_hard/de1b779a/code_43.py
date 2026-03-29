from collections import defaultdict

def dp(dough_left, stuffings_used):
    if dough_left == 0:
        return 0
    if all(stuffing[0] <= 0 for stuffing in stuffings):
        # All stuffings have been used. Consider making a bun without stuffing.
        return max(0, dp(d0, True) + d0)

    profits = []
    for i, (ai, bi, ci, di) in enumerate(stuffings):
        if ai > 0:
            # This stuffing is still available. Calculate the profit.
            profit = di - bi
            remaining_dough = dough_left - ci
            remaining_stuffs = [(a - b, s) for a, b, c, d in stuffings]
            profits.append(profit + dp(remaining_dough, True))
        else:
            # This stuffing is not available. Consider not using it.
            profits.append(dp(d0, False))

    return max(profits)

n, m, c0, d0 = [int(x) for x in input().split()]
stuffings = [[*map(int, input().split())] for _ in range(m)]

print(dp(n, False))

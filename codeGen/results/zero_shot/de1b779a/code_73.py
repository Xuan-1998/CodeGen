profit = 0

for ai, bi, ci, di in a:
    if n >= ci:  # enough dough for at least one bun
        num_buns_without_stuffing = min(n // c0, (n - ci) // bi)
        profit += num_buns_without_stuffing * d0 + (n % c0) * d0 / c0
        n -= num_buns_without_stuffing * c0

    if ai > 0 and n >= ci:  # enough dough and stuffing for at least one bun
        num_buns_with_stuffing = min(n // ci, ai // bi)
        profit += num_buns_with_stuffing * di + (n % ci) * d0 / c0
        n -= num_buns_with_stuffing * ci

print(profit)

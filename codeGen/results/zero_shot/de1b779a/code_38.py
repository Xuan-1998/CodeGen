stuffings.sort(key=lambda x: x[2])
total_profit = 0
for ai, bi, ci, di in stuffings:
    buns_made = min(n//ci, ai//bi)
    total_profit += buns_made * di
    n -= buns_made * ci
    ai -= buns_made * bi
print(total_profit)

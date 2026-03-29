code
n, m, c0, d0 = map(int, input().split())
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())

total_profit = 0
remaining_dough = c0

for i in range(m):
    ai_left = ai
    bi_required = bi
    ci_required = ci
    di_selling_price = di
    buns_made = min(remaining_dough // ci, ai)
    total_profit += (di * buns_made) - (bi * buns_made)
    remaining_dough -= (ci * buns_made)

if remaining_dough > 0:
    buns_made = min(remaining_dough // c0, d0)
    total_profit += (d0 * buns_made) - (c0 * buns_made)

print(total_profit)

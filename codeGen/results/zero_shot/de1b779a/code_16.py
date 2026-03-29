n, m, c0, d0 = map(int, input().split())
stuffed_left = [list(map(int, input().split())) for _ in range(m)]
c = sorted([c0] + [ci for ai, bi, ci, di in stuffed_left], reverse=True)
d = sorted([d0] + [di for ai, bi, ci, di in stuffed_left], reverse=True)

max_profit = 0
buns_made = 0
for i in range(len(c)):
    if c[i] >= (n - sum(ci for ai, bi, ci, di in stuffed_left) + bi) // ci and d[i] > 0:
        buns_made += min((n - sum(ci for ai, bi, ci, di in stuffed_left) + bi) // ci, d[i])
        max_profit += d[i]
    else:
        break

print(max_profit)

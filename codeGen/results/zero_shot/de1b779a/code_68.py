n, m, c0, d0 = map(int, input().split())
buns_without_stuffing = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    buns_without_stuffing.append((ai, bi, ci, di))

max_profit = []
for i in range(n):
    if c0 > 0:
        # Calculate profit for making a bun without any stuffing
        max_profit.append(d0 - (c0 * (i + 1)))
    else:
        break

for i, (ai, bi, ci, di) in enumerate(buns_without_stuffing):
    while ai >= 0 and bi > 0 and ci <= n:
        # Calculate profit for making a bun with the i-th stuffing
        max_profit.append(di - ((bi * (i + 1)) / ci))
        ai -= bi
        bi -= bi
    if ai < 0:
        break

print(max(max_profit))

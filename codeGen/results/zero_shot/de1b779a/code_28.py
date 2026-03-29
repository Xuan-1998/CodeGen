a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

profit_to_dough_ratio = [(di - bi) / ci for i in range(len(d))]
sorted_indices = sorted(range(len(d)), key=lambda i: profit_to_dough_ratio[i], reverse=True)

total_profit = 0

for i in sorted_indices:
    if a[i] >= b[i]:
        num_buns = min(a[i] // c[i], b[i] // c[i])
        total_profit += d[i] * num_buns
        a[i] -= c[i] * num_buns
        if a[i] < b[i]:
            break

print(total_profit)

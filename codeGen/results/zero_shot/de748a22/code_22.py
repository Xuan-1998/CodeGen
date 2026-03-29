import sys

n, q = map(int, input().split())
signs = list(input())

cumulative_sum = 0
for sign in signs:
    if sign == '+':
        cumulative_sum += 1
    else:
        cumulative_sum -= 1

for _ in range(q):
    l, r = map(int, input().split())
    cumulative_sum_l = cumulative_sum - (r // 2) * 2
    cumulative_sum_r = cumulative_sum - (l // 2) * 2

    if cumulative_sum_l > 0 and cumulative_sum_r < 0:
        print((r - l + 1) // 2)
    elif cumulative_sum_l < 0 and cumulative_sum_r > 0:
        print((r - l + 1) // 2)
    else:
        print(0)

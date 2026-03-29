n, q = map(int, input().split())
signs = list(input())
prefix_sum = [0]
for sign in signs:
    if sign == '+':
        prefix_sum.append(prefix_sum[-1] + 1)
    else:
        prefix_sum.append(prefix_sum[-1] - 1)

for _ in range(q):
    l, r = map(int, input().split())
    prefix_sum_left = prefix_sum[l-1]
    prefix_sum_right = prefix_sum[r]
    if prefix_sum_left < 0 and prefix_sum_right > 0:
        print(r - l + 1)
    elif prefix_sum_left < 0:
        print(l - prefix_sum_left - 1)
    else:
        print(r - prefix_sum_right + 1)

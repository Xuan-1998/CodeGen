import sys

n, q = map(int, input().split())
signs = list(input())
cum_sum_signs = [0] * (n + 1)
abs_val_sum = [0] * (n + 1)

for i in range(n):
    cum_sum_signs[i + 1] = cum_sum_signs[i] + 1 if signs[i] == "+" else cum_sum_signs[i] - 1
    abs_val_sum[i + 1] = abs_val_sum[i] + abs(1 if signs[i] == "+" else -1)

for _ in range(q):
    l, r = map(int, input().split())
    diff_sign_sum = cum_sum_signs[r] - cum_sum_signs[l]
    result = abs_val_sum[r] - abs_val_sum[l]
    if diff_sign_sum > 0:
        result += diff_sign_sum
    print(result)

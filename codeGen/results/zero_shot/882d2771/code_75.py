import sys

def calculate_f(n):
    # Implement your dynamic programming solution here to calculate f(n)
    pass

t, l, r = map(int, input().split())

f_l = calculate_f(l)
f_lr = calculate_f(r)

sum = 0
for i in range(t):
    sum += (i + 1) * f_lr - l * f_l if i < t - 1 else -l * f_l

print(sum % (10**9 + 7))

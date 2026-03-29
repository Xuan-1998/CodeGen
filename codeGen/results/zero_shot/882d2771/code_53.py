import sys

t, l, r = map(int, input().split())

# Calculate f(l) and f(r)
f_l = 0  # Initialize f(l)
for i in range(1, l):
    f_l += 1  # Add the number of comparisons needed to select the most beautiful girl from each group
f_r = 0  # Initialize f(r)
for i in range(l, r + 1):
    f_r += 1  # Add the number of comparisons needed to select the most beautiful girl from each group

# Calculate the expression
expression = 0
for i in range(t):
    if i == 0:
        expression += t0 * f_l
    else:
        expression += ti * f_l + (t - i) * (f_r - f_l)
expression -= l * f_r

# Calculate modulo 109 + 7
result = expression % (10**9 + 7)

print(result)

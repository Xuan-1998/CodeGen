# Read input
t, l, r = map(int, input().split())

# Initialize variables
f_l = 0  # f(l)
f_r = 1  # f(r)
result = 0  # t0·f(0) + t1·f(1) + ... + tr - l·f(r)

# Calculate the value of the expression
for i in range(t):
    result += (i % 2 == 0) * f_l + (i % 2 != 0) * f_r
    f_l, f_r = f_r, (f_r + i) % (r - l + 1)

# Print the answer
print(result % (10**9 + 7))

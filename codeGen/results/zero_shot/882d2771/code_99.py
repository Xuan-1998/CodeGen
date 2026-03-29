# Receive input from stdin
t, l, r = map(int, input().split())

# Initialize the variables we'll need
f_sum = 0
l_times_f = 0
base = (1 + 2 + ... + l)

# Calculate f(l), f(l+1), ..., f(r)
for i in range(l, r+1):
    # f(i) is the minimal total number of pairwise comparisons needed to select the most beautiful participant from i girls
    # We know that f(1) = 0 because we just need one comparison to select the most beautiful girl
    # For i > 1, f(i) = i - 1 + min(f(j) for j in range(2, i)) because we can compare i-1 girls first and then select the most beautiful girl from the remaining girls
    f_sum += (i - l) * min((f_sum // base) % (10**6), (r - i) * i)
    l_times_f += (i - l)

# Calculate the expression t0·f(l) + t1·f(l+1) + ... + tr - l·f(r)
expression = sum(t * f for f in range(f_sum, 0, -base)) % (10**9 + 7)

# Print the answer to stdout
print(expression)

# Step 1: Understand the problem
# f(n) is the minimal total number of pairwise comparisons needed to select the most beautiful participant from n girls in a beauty contest
# We need to calculate t0·f(l) + t1·f(l + 1) + ... + tr - l·f(r) modulo 109 + 7

# Step 2: Realize that f(n) is equal to the number of ways to choose n-1 partitions in a sequence of n girls
# This can be calculated using dynamic programming

t, l, r = map(int, input().split())

# Initialize a list to store the values of f(n)
f = [0] * (r + 1)

# Calculate the values of f(n) using dynamic programming
for i in range(2, r + 1):
    f[i] = f[i - 1] + i

# Calculate the value of the expression t0·f(l) + t1·f(l + 1) + ... + tr - l·f(r)
result = (t[0] * f[l]) % (10**9 + 7)
for i in range(1, r):
    result += (t[i] * f[l + i]) % (10**9 + 7)
result -= (l * f[r]) % (10**9 + 7)

# Print the result
print(result)

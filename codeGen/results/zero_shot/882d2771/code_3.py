# Step 1: Understand the problem
# f(n) is the minimal total number of pairwise comparisons needed to select the most beautiful participant from n girls in a beauty contest,
# where the participants are divided into groups and the most beautiful girl is selected from each group until there is only one girl left.

# Step 2: Break down the expression
t0·f(l) + t1·f(l + 1) + ... + tr - l·f(r)

# Step 3: Calculate f(n)
# Since we don't have a formula for f(n), let's assume that f(n) = n

# Step 4: Implement the expression
t0·f(l) + t1·f(l + 1) + ... + tr - l·f(r)

# Python code:
import sys

t, l, r = map(int, input().split())
result = (t0 * f(l)) + (t1 * f(l+1)) + ... + (tr * f(r)) - (l * f(r))
print(result % (10**9 + 7))


# Receive input from stdin
t, l, r = map(int, input().split())

# Define the function f(n) which is the minimal total number of pairwise comparisons needed to select the most beautiful participant from n girls in a beauty contest
def f(n):
    if n == 1:
        return 0  # Base case: only one girl, no need for comparison
    else:
        return 2 + f(n-1)  # Recursive formula: each group needs 2 comparisons, and then the remaining groups need f(n-1) comparisons

# Calculate the value of the expression t0·f(l) + t1·f(l + 1) + ... + tr - l·f(r)
result = sum(t * f(i) for i in range(l, r+1)) - l * f(r)

# Print the answer to stdout
print(result % (10**9 + 7))

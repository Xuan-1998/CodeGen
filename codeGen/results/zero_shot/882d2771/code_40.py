# Read input
t, l, r = map(int, input().split())

# Define f(n) as the minimal total number of pairwise comparisons needed
def f(n):
    if n <= 1:
        return 0
    else:
        # For now, assume we know the answer for n-1 and n-2
        # We can calculate it later when we have a function to compute f(n)
        pass

# Calculate the value of the expression t0·f(l) + t1·f(l + 1) + ... + tr - l·f(r), calculated modulo 109 + 7
result = ((t * f(l)) % (10**9 + 7)) + ((t * f(l+1)) % (10**9 + 7)) + ... + ((t * f(r)) % (10**9 + 7)) - (l * f(r)) % (10**9 + 7)
print(result)

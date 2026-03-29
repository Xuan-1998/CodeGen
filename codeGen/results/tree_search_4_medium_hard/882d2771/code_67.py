# Define the function to calculate f(n)
def f(n):
    if n == 1:
        return 0
    if memo[n] > 0:
        return memo[n]
    max_group = (n + k - 1) // k
    result = f(max_group) + (max_group * (max_group - 1) // 2)
    memo[n] = result % mod
    return memo[n]

# Initialize the memoization table and the modular value
memo = {1: 0}
mod = 10**9 + 7

# Read the input values
t, l, r = map(int, input().split())

# Calculate the expression t0·f(l) + t1·f(l + 1) + ... + tr - l·f(r), calculated modulo mod
result = 0
for i in range(t):
    result += (i % mod) * f(l + i)
result -= l * f(r) % mod
print(result % mod)


# Receive input
t, l, r = map(int, input().split())

# Calculate f(n) for each value of n from l to r
f = [0] * (r + 1)
for i in range(l, r + 1):
    f[i] = min(i, 1)

# Calculate the expression t0·f(1) + t1·f(2) + ... + tr - l·f(r) modulo 109 + 7
result = 0
for i in range(t):
    result += i * f[l + i]

# Print the result
print(result % (10**9 + 7))

def solve(t, l, r):
    # Initialize the prefix sum array
    f = [0] * (r + 1)
    for i in range(l, r + 1):
        f[i] = i // 2 ** 2

    # Calculate the expression value modulo 109 + 7
    res = 0
    for i in range(t):
        res += t**i * f[l + i] % (10**9 + 7)
    return res - l * f[r] % (10**9 + 7)

# Receive input from stdin
t, l, r = map(int, input().split())

# Calculate and print the result
print(solve(t, l, r))

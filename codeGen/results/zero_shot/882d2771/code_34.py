def solve(t, l, r):
    result = 0
    for i in range(t):
        if i == 0:
            result += t0 * f(l)
        else:
            result += ti * f(l + i)
    return result - l * f(r)

# Example usage:
t0 = 1
ti = 2
l = 3
r = 5
print(solve(t, l, r))  # Output: <insert answer here>

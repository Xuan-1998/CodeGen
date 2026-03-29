import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# Sort the array and bad primes
a.sort()
b.sort()

# Initialize maximum beauty
max_beauty = 0

# Iterate through the array
for i in range(n):
    s = a[i]
    # Find the minimum prime divisor p
    for p in range(2, int(s ** 0.5) + 1):
        if all(p % x != 0 for x in b) and s % p == 0:
            break
    else:
        p = s

    # Apply the function f(s)
    beauty = 0
    while s > 1:
        if p not in b:
            beauty += s
        s //= p

    # Update maximum beauty
    max_beauty = max(max_beauty, beauty)

print(max_beauty)

# Read input
n, k = map(int, input().split())
s = input().strip()

if k >= n:
    # If k is greater than or equal to n, just duplicate s until we reach length k
    print(s * (k // n) + s[:k % n])
else:
    # If k is less than n, consider two cases: either delete the last character of s,
    # or duplicate s up to the (k-1)th character. Then compare these two strings and return the smaller one.
    first = s[:-1] * (k // (n - 1)) + s[:k % (n - 1)]
    second = s * (k // n) + s[k % n]
    print(min(first, second))

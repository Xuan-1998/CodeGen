import sys
from functools import lru_cache

# Read input
n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
bad_primes = list(map(int, sys.stdin.readline().strip().split()))

# Define the beauty function
@lru_cache(None)
def beauty(s):
    p = next((p for p in range(2, int(s**0.5) + 1) if s % p == 0), None)
    if p not in bad_primes:
        return beauty(s // p) + s
    else:
        return beauty(s // p) - s

# Calculate the maximum beauty
max_beauty = max(beauty(i) for i in arr)

print(max_beauty)

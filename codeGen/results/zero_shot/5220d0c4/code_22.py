import sys

# Read input
n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
bad_primes = set(map(int, sys.stdin.readline().split()))

# Preprocess bad primes
# ...

# Calculate beauty for each element
beauties = []
for num in array:
    # calculate minimum prime divisor and check if it's good or bad
    # ...
    beauties.append(beauty)

# Find maximum beauty
max_beauty = max(beauties)
print(max_beauty)

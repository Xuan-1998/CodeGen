import sys
from math import gcd
from functools import reduce

def max_beauty(n, m, arr, bad_primes):
    # Calculate GCD for each pair of elements in the array
    gcds = [[arr[i], arr[j]] if i < j else [0] for i in range(n) for j in range(i+1, n)]
    gcds = [(a, b, gcd(a, b)) for a, b in gcds]

    # Sort the GCDs by their values
    gcds.sort(key=lambda x: x[2])

    # Initialize maximum beauty and current beauty
    max_beauty = 0
    curr_beauty = 0

    # Iterate through the sorted GCDs
    for i in range(len(gcds)):
        a, b, _ = gcds[i]
        
        # Calculate the new beauty if we replace (a, b) with their GCD
        new_beauty = curr_beauty - a - b + gcd(a, b)

        # Update the maximum and current beauty if needed
        max_beauty = max(max_beauty, new_beauty)
        curr_beauty = new_beauty

    return max_beauty


# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = set(map(int, sys.stdin.readline().split()))

# Print the maximum beauty to stdout
print(max_beauty(n, m, arr, bad_primes))

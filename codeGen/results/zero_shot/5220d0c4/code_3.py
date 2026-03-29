import sys
from math import sqrt

# Read the size of the array and the number of bad prime numbers
n, m = map(int, sys.stdin.readline().split())

# Read the elements of the array
arr = list(map(int, sys.stdin.readline().split()))

# Read the bad prime numbers
bad_primes = list(map(int, sys.stdin.readline().split()))

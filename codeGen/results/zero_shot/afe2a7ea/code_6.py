import sys
from math import comb

n = int(sys.stdin.readline())

# Calculate the total number of binary strings of length n
total_ways = 2 ** n

print(total_ways % 998244353)

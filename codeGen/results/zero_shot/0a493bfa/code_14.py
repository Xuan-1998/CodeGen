import sys
from math import gcd as math_gcd
from functools import reduce
from collections import deque

# Function to calculate the beauty of an array
def calc_beauty(arr):
    n = len(arr)
    res = 0
    queue = deque([(n, arr)])
    
    while queue:
        size, nums = queue.popleft()
        
        # Calculate the beauty for this subset
        new_beauty = sum(math_gcd.reduce(lambda x, y: math_gcd(x, y), nums))
        
        # Update the result
        res += new_beauty
        
        if size > 1:
            for i in range(size):
                queue.append((i + 1, [math_gcd(*nums[:i]), *nums[i+1:]]))
    
    return res

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

# Calculate the maximum beauty
print(calc_beauty(arr))

from collections import defaultdict
import sys

# Initialize a defaultdict for memoization
memo = defaultdict(int)

def fib(n):
    # Base cases for the Fibonacci sequence
    if n == 0:
        return 0
    if n == 1:
        return 1
    # If the value has not been computed, store it in the memo dictionary
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    # Return the stored value
    return memo[n]

# Read input from stdin
n = int(sys.stdin.readline().strip())

# Calculate and print the Fibonacci number to stdout
print(fib(n))

import sys

# Read input from standard input
n, x = map(int, sys.stdin.readline().split())

# Calculate the number of digits in the decimal representation of x
current_digits = 0
while x > 0:
    x //= 10
    current_digits += 1

# If the length of the decimal representation of x is already n or more, return -1
if current_digits >= n:
    print(-1)
else:
    # Calculate the minimum number of operations required to make the length of decimal representation of x equal to n
    min_operations = n - current_digits
    
    # Print the result to standard output
    print(min_operations)
